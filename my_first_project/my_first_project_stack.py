from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as _s3,
    aws_iam as _iam,
    CfnOutput,
    Token
    # aws_sqs as sqs,
)
from constructs import Construct

class MyFirstProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MyFirstProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        _s3.Bucket(
            self, 
            "MyFirstProjectBucket",
            bucket_name="my-first-project-bucket-12345",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket = _s3.Bucket(
            self,
            "myBucketid"
        )

        snstopicname = "mySNSTopic"

        if not Token.is_unresolved(snstopicname) and len(snstopicname) > 10:
            raise ValueError("Maximum length of SNS topic name must be 10 or less")

        print(mybucket.bucket_name)

        _iam.Group(
            self,
            "gid"
        )

        output_1 = CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My first CDK bucket",
            export_name="myBucketOutput1"
        )