import boto3
from pprint import pprint
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def change_asg_capacity(aws_mag_con, autoscaling_group_names):
	try:
		asg_client = aws_mag_con.client('autoscaling')
		for asg_ in autoscaling_group_names:
			response1 = asg_client.update_auto_scaling_group(
			AutoScalingGroupName = asg_,
			MinSize=0,
			DesiredCapacity=0
			)
			print('Desired Capacity for "{}" changed to 0.'.format(asg_))

	except Exception as e:
	        logger.error('Something went wrong: ' + str(e))
