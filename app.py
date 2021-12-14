#!/usr/bin/env python3

import aws_cdk as cdk

from my_python_sample.my_python_sample_stack import MyPythonSampleStack


app = cdk.App()
MyPythonSampleStack(app, "my-python-sample")

app.synth()
