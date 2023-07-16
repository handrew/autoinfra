# Infra GPT

## Overview

Infra GPT was an attempt to give 


## Usage

1. `git clone https://github.com/handrew/agentic_gpt`

2. Move `infra_gpt.py` into the cloned folder

3. `cd` into the folder and then `python infra_gpt.py`. You have to have AWS credentials on your local machine. 


## Output

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
INFO:agentic_gpt.agent.agentic_gpt:Completed action ssh_and_xecute_cmd. Result: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">                                        
                                                                                                                                                                                                                   
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
INFO:agentic_gpt.agent.agentic_gpt:Reasoning: The task requires me to print the response from the server after making the HTTP request. The response is already stored in the memory as a result of the ssh_and_exe
cute_cmd action. After printing the response, I will declare the task as done.
```
