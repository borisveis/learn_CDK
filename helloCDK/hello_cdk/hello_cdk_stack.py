from aws_cdk import (
    aws_ec2 as ec2,
    App, Stack
)
from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "MyVpc",
                      max_azs=3  # Default is all AZs in the region
                      )
        # Define an EC2 instance
        instance1 = ec2.Instance(self, "MyInstance1",
                                instance_type=ec2.InstanceType("t2.micro"),
                                machine_image=ec2.MachineImage.latest_amazon_linux2(),
                                vpc=vpc
                                )
        instance2 = ec2.Instance(self, "MyInstance2",
                                 instance_type=ec2.InstanceType("t2.micro"),
                                 machine_image=ec2.MachineImage.latest_amazon_linux2(),
                                 vpc=vpc
                                 )
