import boto3
from pprint import pprint
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def list_eks_cluster(client, region_name):
    try:
        response = client.list_clusters()
        clusters = response["clusters"]
        print("Clusters for region {0}: {1}".format(region_name,clusters))
        return clusters

    except Exception as e:
        pprint(e)

def list_node_groups(client, eks_cluster):
    nodegroup_list = []
    try:
        response = client.list_nodegroups(clusterName=eks_cluster)
        nodegroup_list = response['nodegroups']
        print('Node groups for cluster {0}: {1}'.format(eks_cluster, nodegroup_list))

        return nodegroup_list
        #list_asg_from_eks_nodegroup(client, eks_cluster, nodegroup_list)
    except Exception as e:
        print(e)

def list_asg_from_eks_nodegroup(client, cluster, nodegroup_list):
    list_asg = []
    try:
        for node in nodegroup_list:
            response = client.describe_nodegroup(clusterName=cluster,nodegroupName=node)
            print("For Node Group {}".format(node))
            for asg in response['nodegroup']['resources']['autoScalingGroups']:
                asg_name = asg['name']
                list_asg.append(asg_name)
                print("ASG {} appended to the list.".format(asg_name))
        return list_asg
    except Exception as e:
        print(e)
