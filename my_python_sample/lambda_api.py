from constructs import Construct
from aws_cdk import (
    App, Stack,
    aws_lambda as _lambda,
    aws_apigateway as _apigw,
    aws_ecr as ecr
)


class ApiCorsLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repository = ecr.Repository.from_repository_name(
            self,
            "sample-service",
            repository_name="sample-service"
        )

        base_lambda = _lambda.DockerImageFunction(
            self,
            'ApiCorsLambda',
            code=_lambda.DockerImageCode.from_ecr(
                repository=repository,
                tag="3.0.0"
            )
        )

        base_api = _apigw.RestApi(
            self,
            'ApiGatewayWithCors',
            rest_api_name='ApiGatewayWithCors'
        )

        deployment = _apigw.Deployment(self, "Staging", api=base_api)

        example_entity = base_api.root.add_resource(
            'example',
            default_cors_preflight_options=_apigw.CorsOptions(
                allow_methods=['GET', 'OPTIONS'],
                allow_origins=_apigw.Cors.ALL_ORIGINS)
        )
        example_entity_lambda_integration = _apigw.LambdaIntegration(
            base_lambda,
            proxy=False,
            integration_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Origin': "'*'",
                }
            }]
        )
        example_entity.add_method(
            'GET', example_entity_lambda_integration,
            method_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Origin': True,
                }
            }]
        )


app = App()
ApiCorsLambdaStack(app, "ApiCorsLambdaStack")
app.synth()