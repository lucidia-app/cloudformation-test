from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
)


class S3Buckets(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        style_transfer_bucket = s3.Bucket(
            self,
            "StyleTransferBucket",
            versioned=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )
