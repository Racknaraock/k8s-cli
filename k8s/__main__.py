import click
from kubernetes import client,config
from .dc import Dc

def set_up_client_v1_api():
    print("Loading your local kubeconfig")
    config.load_kube_config()
    return client.AppsV1Api()
    

@click.group()
@click.version_option(version='1.0.0')
def tables():
    pass

#TODO:mirar como meter opcion de shorting dentro de los parametros de entrada
@tables.command()
@click.option('-S', is_flag=True, help="Short the results by time descending")
@click.option('--namespace',help='Define the namespace to get the tables values')
def show(**kwargs):
    v1=set_up_client_v1_api()

    if(kwargs.get("namespace",False)):
        ret = v1.list_namespaced_deployment(kwargs.get("namespace"))
    else:
        ret = v1.list_deployment_for_all_namespaces()


    dc_list = []
    
    print("|| Name || Image || Last Update Time || Status ||")
    print("="*111)

    for i in ret.items:
        dc_list.append(Dc(i))

    if(kwargs.get("S")):
        dc_list=sorted(dc_list, key=lambda d: d.last_update,reversed=True)

    for i in dc_list:
        print(i)
    print("="*111)

if __name__ == '__main__':
    tables()