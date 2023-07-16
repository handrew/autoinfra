# 🔩 AutoInfraGPT

*by Adi Prerepa and Andrew Han*

## Overview

AutoInfraGPT was an attempt to create an LLM agent (using an [AGI architecture](https://github.com/handrew/agentic_gpt) that we built ahead of time) with the capability of creating an EC2 instance on Amazon, SSHing into it, and then running a `curl` command on the EC2 instance to a separate server.

The main logic of the code is shown below:

```python
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
    objective, actions_available=actions, model="gpt-4"
)
agent.run()
```

where `create_ec2_instance` is a function we wrote to spin up an AWS VM and `ssh_and_execute_cmd` is another function we wrote to `SSH` into the created instance and run a UNIX command. 

The agent is instantiated with `actions` and given the objective to "Create 1 EC2 Instance with name rat. Ssh into that instance and make HTTP request via curl to http://54.245.39.114:8080. Print the response from the server. Declare done." 

The hardcoded endpoint hosts a Python server which returns a simple HTML. GPT-4 and `AgenticGPT` should, given the instructions, know to call the two functions in order, resulting in a `curl` reuquest to the given endpoint. See the output below to see the output from the agent.

## Future Possibilities

This was a trivial example that involved two steps, with calls to two functions. However, you could imagine exposing many more of AWS's APIs to `AgenticGPT`, giving it the ability to use more resources, read logs, and respond accordingly. Taken as a whole, we could conceivably see a world in which devops are automated by agents. 


## Usage

1. `git clone https://github.com/handrew/agentic_gpt`

2. Move `autoinfra_gpt.py` into the cloned folder (sorry! `AgenticGPT` is not yet on pypi)

3. Set up a `.env` file with `OPENAI_API_KEY` with your API key and `SSH_KEYFILE` with AWS SSH key.

4. `cd` into the folder and then `python autoinfra_gpt.py`. You have to have AWS credentials on your local machine. 


## Output (of a successful run)

```
INFO:agentic_gpt.agent.agentic_gpt:Taken steps 1 of maximum 100.                                                                                                                                                   
INFO:agentic_gpt.agent.agentic_gpt:                                                                                                                                                                                
                                                                                                                                                                                                                   
Thoughts: I need to create an EC2 instance first. I will use the create_ec2_instance action with the instance_name as 'rat' and instance_count as 1.                                                               
INFO:agentic_gpt.agent.agentic_gpt:Reasoning: The first step in the objective is to create an EC2 instance with the name 'rat'. This can be achieved using the create_ec2_instance action.                         
INFO:agentic_gpt.agent.agentic_gpt:Chosen action: create_ec2_instance                                                                                                                                              
INFO:botocore.credentials:Found credentials in shared credentials file: ~/.aws/credentials                                                                                                                         
INFO:botocore.credentials:Found credentials in shared credentials file: ~/.aws/credentials                                                                                                                         
INFO:agentic_gpt.agent.agentic_gpt:Completed action create_ec2_instance. Result: ec2-54-213-51-236.us-west-2.compute.amazonaws.com                                                                                 
INFO:agentic_gpt.agent.agentic_gpt:Taken steps 2 of maximum 100.                                                                                                                                                   
INFO:agentic_gpt.agent.agentic_gpt:                                                                                                                                                                                
                                                                                                                                                                                                                   
Thoughts: Now that the EC2 instance is created, I need to SSH into it and make an HTTP request to the provided URL. I will use the curl command for this.                                                          
INFO:agentic_gpt.agent.agentic_gpt:Reasoning: The next step in the task is to SSH into the created EC2 instance and make an HTTP request. The curl command is a tool to transfer data from or to a server, using on
e of the supported protocols. In this case, we are using it to make an HTTP request.                                                                                                                               
INFO:agentic_gpt.agent.agentic_gpt:Chosen action: ssh_and_execute_cmd                                                                                                                                              
sshing with: {}, username {}  ec2-54-213-51-236.us-west-2.compute.amazonaws.com ec2-user                                                                                                                           
INFO:paramiko.transport:Connected (version 2.0, client OpenSSH_8.7)                                                                                                                                                
INFO:paramiko.transport:Authentication (publickey) successful!                                                                                                                                                     
INFO:agentic_gpt.agent.agentic_gpt:Completed action ssh_and_execute_cmd. Result: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">                                        
                                                                                                                                                                                                                   
<html>                                                                                                                                                                                                             
                                                                                                                                                                                                                   
<head>                                                                                                                                                                                                             
                                                                                                                                                                                                                   
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">                                                                                                                                                
                                                                                                                                                                                                                   
<title>Directory listing for /</title>                                                                                                                                                                             
                                                                                                                                                                                                                   
</head>                                                                                                                                                                                                            
                                                                                                                                                                                                                   
<body>

<h1>Directory listing for /</h1>

<hr>

<ul>
<li><a href=".bash_history">.bash_history</a></li>

<li><a href=".bash_logout">.bash_logout</a></li>

<li><a href=".bashrc">.bashrc</a></li>

<li><a href=".cache/">.cache/</a></li>

<li><a href=".profile">.profile</a></li>

<li><a href=".python_history">.python_history</a></li>

<li><a href=".ssh/">.ssh/</a></li>

<li><a href=".sudo_as_admin_successful">.sudo_as_admin_successful</a></li>

</ul>

<hr>

</body>

</html>

INFO:agentic_gpt.agent.agentic_gpt:Taken steps 3 of maximum 100.
INFO:agentic_gpt.agent.agentic_gpt:

Thoughts: I have created the EC2 instance and made the HTTP request via curl. The response from the server is stored in the memory. Now, I need to print the response and declare the task as done.
INFO:agentic_gpt.agent.agentic_gpt:Reasoning: The task requires me to print the response from the server after making the HTTP request. The response is already stored in the memory as a result of the ssh_and_execute_cmd action. After printing the response, I will declare the task as done.
```
