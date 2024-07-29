import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2
)
from constructs import Construct

class MyEc2Instance(ec2.Instance):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # Define any custom parameters you want to add
        custom_instance_type = kwargs.get("t2.micro", ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO))
        custom_machine_image = kwargs.get('machine_image', ec2.MachineImage.latest_amazon_linux())

        # Call the parent constructor with custom or default parameters
        super().__init__(
            scope,
            id,
            instance_type=custom_instance_type,
            machine_image=custom_machine_image,
            **kwargs
        )
