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


def create_ec2_instance(instance_name, instance_size):
    """Create an EC2 instance with `instance_name` and `instance_size`."""
    raise NotImplementedError("TODO")


def ssh_into_instance(hostname, username):
    ssh = paramiko.SSHClient()

    keyfile = os.path.expanduser(os.environ["SSH_KEYFILE"])
    with open(keyfile, "r") as f:
        keyfile = StringIO(f.read())
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

    objective = f"""Create and deploy a version of yourself onto five servers
and make sure that one server is running at all times."""

    agent = AgenticGPT(
        objective, actions_available=actions, model="gpt-3.5-turbo-16k"
    )
    agent.run()


if __name__ == "__main__":
    ssh = ssh_into_instance(hostname="164.92.91.161", username="root")
    import pdb; pdb.set_trace()