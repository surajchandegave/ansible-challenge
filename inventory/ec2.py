#!/usr/bin/python

import argparse
import boto3
import json
import os
import sys

region = os.environ.get('AWS_REGION', None)

if region is None:
    print("$AWS_REGION must be set")
    sys.exit(1)

parser = argparse.ArgumentParser(description='Dynamic inventory for ec2 insatnces')
parser.add_argument('--list', help="list hosts", action="store_true")
parser.add_argument('--host', help="list host vars")
args = parser.parse_args()

if args.host:
  print("{}")

if not args.list:
  sys.exit(1)

session = boto3.Session(region_name=region)
ec2 = session.resource('ec2', region)

instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}, {'Name': 'tag:purpose', 'Values': ['online_games']}])

inventory = {"_meta": {"hostvars": {}}}
inventory["online_games_instances"] = { "hosts": [] }
ips = []
for instance in instances:
  print(instance.id, instance.instance_type, instance.public_ip_address)
  print("%s" %instance)
  ips.append(instance.public_ip_address)

inventory["online_games_instances"]["hosts"] = ips
  
print(json.dumps(inventory))
