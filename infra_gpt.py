"""Use AgenticGPT to muck with infar."""
import os
from dotenv import load_dotenv
import paramiko
from io import StringIO

load_dotenv()
from agentic_gpt.agent import AgenticGPT
from agentic_gpt.agent.utils.llm_providers import get_completion
from agentic_gpt.agent.action import Action
from playwright.sync_api import sync_playwright


def create_ec2_instance(instance_name, instance_count):
    s = boto3.Session(region_name="us-west-2")
    ec2_session = s.resource('ec2')
    ec2 = boto3.client('ec2')
    # Define the AMI ID, instance type, and other parameters
    ami_id = 'ami-0507f77897697c4ba'
    instance_type = 't2.micro'
    key_name = 'ssh'

    # Create the instance
    instances = ec2_session.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        MinCount=instance_count,
        MaxCount=instance_count,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name,
                    },
                ]
            },
        ],
    )
    for instance in instances:
        instance.wait_until_running()


def ssh_into_instance(hostname, username):
    ssh = paramiko.SSHClient()

    keyfile = os.path.expanduser(os.environ["SSH_KEYFILE"])
    with open(keyfile, "r") as f:
        keyfile = StringIO.StringIO(f.read())
    mykey = paramiko.RSAKey.from_private_key(keyfile)

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, pkey=mykey)
    return ssh


def main():
    actions = [
        Action(
            name="create_ec2_instance",
            description="Create an EC2 instance on Amazon.",
            function=create_ec2_instance,
        ),
        Action(
            name="ssh_into_instance",
            description="SSH into instance",
            function=ssh_into_instance,
        ),
    ]

    objective = f"""Create 1 EC2 Instance"""

    agent = AgenticGPT(
        objective, actions_available=actions, model="gpt-3.5-turbo-16k"
    )
    agent.run()


if __name__ == "__main__":
    main()
