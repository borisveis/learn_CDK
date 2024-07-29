import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    Stack
)
from constructs import Construct
from .Instance_construct import MyEc2Instance

class Custom_instance(ec2.Instance):
    def __init__(self,  **kwargs) -> None:
        # Define any custom parameters you want to add
        custom_instance_type = kwargs.get('instance_type', ec2.InstanceType.of(ec2.InstanceClass.mi, ec2.InstanceSize.MICRO))
        custom_machine_image = kwargs.get('machine_image', ec2.MachineImage.latest_amazon_linux())

        # Call the parent constructor with custom or default parameters
        super().__init__(
            scope,
            id,
            instance_type="t2.micro",
            machine_image=custom_machine_image,
            **kwargs
        )

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
        instance3 =  MyEc2Instance(self, "MyInstance3_useconstruct",
                                                vpc=vpc)
