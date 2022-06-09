from kubernetes import client, config

def __get_kubernetes_client(bearer_token,api_server_endpoint):
    try:
        configuration = client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        client_api = client.BatchV1beta1Api()
        return client_api
    except Exception as e:
        print("Error getting kubernetes client \n{}".format(e))
        return None

def getcronjobs(cluster_details,namespace="default",all_namespaces=True):
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
        )
        if all_namespaces is True:
            

            ret =client_api.list_cron_job_for_all_namespaces(watch=False)
            temp_dict_obj={}
            temp_list_obj=[]
            for i in ret.items:
                temp_dict_obj={
                    "name": i.metadata.name,
                    "namespace": i.metadata.namespace
                }
                temp_list_obj.append(temp_dict_obj)
                print("cronjob under all namespaces: {}".format(temp_list_obj))
            return temp_list_obj
        else:
            cronjob_list = client_api.list_namespaced_cron_job("{}".format(namespace))
            print("cronjob under all namespaces:{}".format(cronjob_list))
            return cronjob_list

if __name__ == "__main__":
    cluster_details={
        "bearer_token":"GKE-Bearer-Token",
        "api_server_endpoint":"ip-k8s-control-plane"
    }
    getcronjobs(cluster_details)