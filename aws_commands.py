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
