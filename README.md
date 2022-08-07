# Ansible Technical Challenge

pip install boto boto3

mkdir -pv ~/.aws/
vi ~/.aws/credentials

[default]
aws_access_key_id = YOUR-ACCESS-KEY-HERE
aws_secret_access_key = YOUR-SECRET-ACCESS-KEY-HERE

vi ~/.aws/config

[default]
region = us-west-1

ansible-vault create group_vars/all/pass.yml
New Vault password:
Confirm New Vault password:

ansible-vault edit group_vars/all/pass.yml 
Vault password:
aws_access_key: AAAAAAAAAAAAAABBBBBBBBBBBB                                      
aws_secret_key: afjdfadgf$fgajk5ragesfjgjsfdbtirhf
