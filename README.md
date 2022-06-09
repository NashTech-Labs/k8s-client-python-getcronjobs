### Python client for the kubernetes API.

### Installation From source:

'''git clone --recursive https://github.com/kubernetes-client/python.git cd'''

python python setup.py install From PyPI directly:

pip install kubernetes

Interacting with Kubernetes Resources

we can use the client module to interact with the resources. Get
Resources: kubectl get commands are used to list all kinds of resources
in a cluster for eg:

-   List nodes: To list all the cronjobs in the cluster, we fire
    following kubectl command:

kubectl get cronjobs \# lists all the cronjobs

In Python, we instantiate BatchV1beta1Api class from client module:

client_api = client.BatchV1beta1Api()

Here I've created the client with it's respective class BatchV1beta1Api
and storing in a var named as client_api. so furture we can use it.

KubeConfig: to pass the on local cluster e.g minikube we use bellow
command: config. load_kube_config()

Authenticating to the Kubernetes API server

but what if you want to list all the automated cronjobs of a GKE Cluster
, you must need to authenticate the configuration

configuration.api_key = {"authorization": "Bearer" + bearer_token} \#
for authentication to the GKE Cluster

I've used Bearer Token which enable requests to authenticate using an
access key,

List the cronjobs in all namespaces:

set if all_namespaces is True:

and run following command:

python3 get-cronjob.py

you'll look like something below

Screenshot from 2022-06-09 13-40-03.png List the cronjobs in default
namespace:

set if all_namespaces is False:

python3 get-cronjob.py

and any specific namespace you can pass getcronjobs() parameter named as
namespace="namespace-name"
