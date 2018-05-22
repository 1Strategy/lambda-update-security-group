import boto3
import json

def lambda_handler(event, context):
    sgarn = (event['resources'][0])
    print(sgarn)
    
    ip_permissions = (event['detail']['configurationItem']['configuration']['ipPermissions'])
    print(ip_permissions)
    
    
    sgID = sgarn.split("/")[1]
    print(sgID)
    
    
    ec2 = boto3.resource('ec2')
    sg = ec2.SecurityGroup(sgID)
    
    response = sg.revoke_ingress(IpPermissions=sg.ip_permissions)
    print(response)