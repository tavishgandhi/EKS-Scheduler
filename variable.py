import boto3
from pprint import pprint
import logging

profile_name = "Tavish"

def get_profile_name():
    return profile_name

def get_custom_regions():
	try:
		list_of_regions = ["us-west-1"]
		return list_of_regions

	except Exception as e:
		logger.error('Something went wrong: ' + str(e))
		return False

def get_all_regions():
    try:
		# Code to fetch all regions
		# all_regions=[]
		# session = boto3.session.Session(profile_name=profile_name, region_name="us-east-1")
		# ec2_client = session.client(service_name="ec2")
		# for each_region in ec2_client.describe_regions()['Regions']:
		# 	all_regions.append(each_region.get('RegionName'))
        all_regions = ['eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-west-1','ap-northeast-3','ap-northeast-2', 'ap-northeast-1', 'sa-east-1', 'ca-central-1','ap-southeast-1', 'ap-southeast-2','eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
        return all_regions

    except Exception as e:
        logger.error("Something went wrong: " + str(e))
        return False
