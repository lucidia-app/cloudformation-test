from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ecr as ecr
)


class Repositories(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        style_transfer_repository = ecr.Repository(
            self,
            "sample-service",
            repository_name="sample-service"
        )
