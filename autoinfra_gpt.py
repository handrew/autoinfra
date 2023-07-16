"""Use AgenticGPT to muck with infar."""
import os
from dotenv import load_dotenv
import paramiko
from io import StringIO
import boto3
load_dotenv()
from agentic_gpt.agent import AgenticGPT
from agentic_gpt.agent.utils.llm_providers import get_completion
from agentic_gpt.agent.action import Action
from playwright.sync_api import sync_playwright
import json

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
        SecurityGroupIds=["sg-0d68b8c7dac2c6e30"],
    )
    for instance in instances:
        instance.wait_until_running()
    inst_with_ip = ec2.describe_instances(InstanceIds=[instance.instance_id for instance in instances])['Reservations'][0]['Instances']
    ips = [inst["PublicDnsName"] for inst in inst_with_ip]
    return ips[0]

def ssh_and_execute_cmd(hostname, command):
    username = "ec2-user"
    print("sshing with: {}, username {} ", hostname, username)
    ssh = paramiko.SSHClient()

    keyfile = os.path.expanduser(os.environ["SSH_KEYFILE"])
    with open(keyfile, "r") as f:
        keyfile = StringIO(f.read())
    mykey = paramiko.RSAKey.from_private_key(keyfile)

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, pkey=mykey)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    return "\n".join(lines)


def main():
    actions = [
        Action(
            name="create_ec2_instance",
            description="Create an EC2 instance on Amazon. Returns the public ipv4 of this instance.",
            function=create_ec2_instance,
        ),
        Action(
            name="ssh_and_execute_cmd",
            description="SSH into an instance and run a command.",
            function=ssh_and_execute_cmd,
        ),
    ]

    objective = f"""Create 1 EC2 Instance with name rat. Ssh into that instance and make HTTP request via curl to http://54.245.39.114:8080. Print the response from the server. Declare done."""

    agent = AgenticGPT(
        objective, actions_available=actions, model="gpt-4",# verbose=True
    )
    agent.run()


if __name__ == "__main__":
    main()
    #ssh = ssh_into_instance(hostname="164.92.91.161", username="root")
    #import pdb; pdb.set_trace()
