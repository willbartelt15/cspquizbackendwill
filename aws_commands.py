# aws_commands.py
import boto3
import time

def run_aws_command(instance, mycommand):
    region = 'us-east-2'
    ssm_client = boto3.client('ssm', region_name=region)
    command = mycommand
    instance_id = instance # 'i-07494ecf4435591be'

    response = ssm_client.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [command]}
    )

    command_id = response['Command']['CommandId']
    time.sleep(8)  # Adjust the sleep time as needed

    output = ssm_client.get_command_invocation(
        CommandId=command_id,
        InstanceId=instance_id
    )
    return output['StandardOutputContent']

def get_ec2_instance_info():
    region_name = 'us-east-2'  # Specify your region
    ec2 = boto3.client('ec2', region_name=region_name)

    # Retrieve information about all EC2 instances
    response = ec2.describe_instances()
    return response