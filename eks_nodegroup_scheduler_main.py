import boto3
from pprint import pprint
import logging
from eks_nodegroup_list import *
from asg_change_desired_capacity import *
from variable import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

profile_name = get_profile_name()
region_name = get_all_regions()

def main():
    try:
        for region in region_name:
            print("Working for region: {}".format(region))
            aws_mag_con = boto3.session.Session(profile_name=profile_name, region_name = region)
            client = aws_mag_con.client('eks')

            # Fetching clusters from a particular region
            print('Fetching clusters from a particular region')
            cluster_list = list_eks_cluster(client, region)

            # Fetching node group list for each cluster
            for cluster in cluster_list:
                nodegroup_list = list_node_groups(client, cluster)

                # Fetching the list of ASG of all nodegroups in the given cluster
                asg_list = list_asg_from_eks_nodegroup(client, cluster, nodegroup_list)

                # Changing the desired capacity of the ASG
                change_asg_capacity(aws_mag_con, asg_list)
                
            print("-------------------------------------------------------------")

    except Exception as e:
        pprint(e)

if __name__ == '__main__':
    main()
