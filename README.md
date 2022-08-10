# Ansible Technical Challenge

This ansible-playbook will help you perform the below task. The playbook maintains the idempotency, so rerunning the playbook would not create multiple EC2 instances
1. Create EC2 key pair
2. Create a security group to open SSH and HTTP port(For simplicity accepts the request from all IPs, and can be restricted to a specific IP range)
3. Deploys EC2 instances to configured AWS region
4. Creates the dynamic inventory to be used by the configuration step
5. Deploys different packages required for setting up the HTTP server
6. Configure the HTTP server on each instance to host the one HTML games
7. Hardens the HTTP server installed

There are 2 roles created to serve different purposes
1. Deployment of EC2 instances and creation of in-memory inventory
2. Configuration of the HTTP server

Below are some of the assumptions/limitations
1. You have access to AWS to deploy EC2 instances(A free tier account is sufficient)
2. Tested with Amazon Linux2 however, should work with Fedora/CentOS/RHEL

Steps to execute this playbook
1. Create an ansible vault and set a password

```
ansible-vault create group_vars/all/pass.yml
New Vault password:
Confirm New Vault password:
```
2. Add AWS access_key and secret_key to the vault
```
ansible-vault edit group_vars/all/pass.yml 
Vault password:
aws_access_key: <AWS ACCESS KEY>                                      
aws_secret_key: <AWS SECRET KEY>
```
3. Update the infrastructure parameters such as image(image id of AMI, preferably Amazon Linux2), AWS region and subnet id under
```
group_vars/infra.yml
```
4. Currently deploys and configures 2 games. If you wish to configure more, update "online_games" under "group_vars/infra.yml" to have the name and link to one HTML game added.

5. Execute an ansible playbook to setup online games
```
ansible-lint site.yml
ansible-galaxy collection install -r collections/requirements.yml
ansible-playbook site.yml --ask-vault-pass
```

P.S. This playbook does not delete EC2 instances deployed. Please make sure you delete them manually from AWS otherwise, it may incur extra cost.
