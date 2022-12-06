#!/usr/bin/python3

import requests
import json
import os
from kubernetes import client, config 

from kubernetes.config import load_kube_config                     

import subprocess

config.load_kube_config()
session = requests.Session()
session.verify = False

#command = 'kubectl apply -f deployment.yaml'



myToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImM1aFVEWEJwSl9Wc3dHUW02Qm5jd3JDdnQ0OVlJbWVpUVFMS041ZGdVWDAifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InNlcnZpY2VhY2NvdW50LXNhLXRva2VuIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6InNlcnZpY2VhY2NvdW50LXNhIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiZDU2NDIyMWEtMTMwNC00NDk5LWI3ZmItZTdiMTc4ODBmZGJmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6c2VydmljZWFjY291bnQtc2EifQ.thHpwvvbSsFFeMB5LUmMP5dSYNOIOIzVOtN-oRbOV14fVd5OLHqwNkCNaWfpMZet24J3D21QtfMIXeNSXmOmfJORLw836r2sXt2IdQ9Sa65mgH0_5YA2mLkkd45zYPQhD-CgxVdjzjKR2TK6GvWX4kejE5napP7aAivtpCyLagRIrw9fQZ7ucYZIwBdnu1XajI8tLGCtWiQ859ydCHmwCkJR_ljU-MULMYXM8fAiC-fjny7BY7oXnVEJ5p_Glz_o8dc_dHhDfv70cImuB2u0XmPYT8hmHN9YqX3ZHaAbw9iicV7IHhojorRwRXh6FoooNZlt09kflVsPIe6js2r6Zg'

data1 = "Authorization: Bearer "
data2 = myToken
data3 = data1 + data2

response = []

response = json.loads(subprocess.check_output([
    'curl',
     '-s',
    '-X',
    'GET',
    'https://kubernetes.docker.internal:6443/apis/metrics.k8s.io/v1beta1/pods',
    '--header',
    data3,
    '--insecure',
    
]))






pods = []

i = 0
data = response["items"]

medata = {}
podname = []
namespace = []
vtimes = []
container = []
cpuusage = []
memusage = []
dict = []

for item in data :
    
    #print('item no= ', i)
    j = i + 1
    medata = response["items"][i]['metadata']
    vtimes.append(str(response['items'][i]["timestamp"]))
    podname.append(medata['name'])
    container.append(response['items'][i]["containers"][0]['name'])
    cpuusage.append(response['items'][i]["containers"][0]['usage']['cpu'])
    memusage.append(response['items'][i]["containers"][0]['usage']['memory'])
   #podname[i] = response["items"][i]['metadata']['name']
    namespace.append(medata['namespace'])
    


   # namespace[i] = response["items"][i]['metdata']['namespace']
    #timestamp.append(medata['timestamp'])
    print("\n")
    
    
    dict = {  "NAMESPACE": namespace[i],"pods-name": podname[i] , "timestamp": vtimes[i] ,"container": container[i], "usage-cpu": cpuusage[i], "usage-mem": memusage[i]}
    #list.append(dict)
    for key, value in dict.items():
        
        if key == "NAMESPACE":

            print(key ,":", value)
            print("--------------------------")
        else:

            print(key ,":", value)


    #print ("pod =", podname[i] , "namespace =", namespace[i], "timestamp =",vtimes[i] ,"container =", container[i], "usage: cpu =", cpuusage[i], "mem =", memusage[i] ) 
    #print ("pod=", podname[i] , "namespace=", namespace[i], "timestamp=", vtimes[i] ) 
    i = i + 1
    #print(list[i])




#timevalue = response['items'][0]['timestamp']
#print ( "timevalue=" ,  )


    
    





#print ("\n printing one item metadata \n", medata)





#pod[] = response["items"][0]['metadata']['name']
#print("Type:", type(json_data))
#print(data)

#print('printing datata now ')
#print(json_data)

#api_client = client.ApiClient()





#pod_logs = v1.read_namespaced_pod_log(name = 'testpod', container = 'testpod', namespace='interview', follow=False)
#pod_logs = v1.read_namespaced_pod_log(name = 'demo-hello-world-es-86bc79b9c8-5z8n5', container = 'demo-hello-world-es', namespace='interview', follow=False)

#print("hello worls")
#v1.list_namespaced_pod(namespace='interview')
#pods =  v1.list_namespaced_pod(namespace='interview')
#print(pods)
#print("printing pod-logs")
#print(pod_logs)

