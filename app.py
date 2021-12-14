#!/usr/bin/env python3

import aws_cdk as cdk

from my_python_sample import MyPythonSampleStack, S3Buckets, Repositories, ApiCorsLambdaStack


app = cdk.App()
MyPythonSampleStack(app, "my-python-sample")
S3Buckets(app, "S3-Buckets")
Repositories(app, "Repositories")
ApiCorsLambdaStack(app, "LambdaAPIStack")


app.synth()
