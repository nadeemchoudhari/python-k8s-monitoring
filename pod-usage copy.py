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
#myToken = subprocess.run( ["kubectl", "get", "secret", "serviceaccount-sa-token" , "-o" , "jsonpath='{.data.token}' | base64 --decode]"])

data1 = "Authorization: Bearer "

data2 = myToken

data3 = data1 + data2

response = {}

response = subprocess.call([
    'curl',
    '-X',
    'GET',
    'https://kubernetes.docker.internal:6443/apis/metrics.k8s.io/v1beta1/pods',
    '--header',
    data3,
    '--insecure'
])

command = str("echo " + response + " |" + " jq")

json_data = os.system(command)

#response = subprocess.run(["echo", response , "|", "jq"])

json_data = json.loads(response)
print("Type:", type(json_data))


#TOKEN=$(kubectl get secret serviceaccount-sa-token -o jsonpath='{.data.token}' | base64 --decode)

api_client = client.ApiClient()


myUrl = 'https://kubernetes.docker.internal:6443/apis/metrics.k8s.io/v1beta1/pods'
head = {'Authorization': 'token {}'.format(myToken)}
#response = api_client.call_api('/apis/metrics.k8s.io/v1beta1/pods', 'GET')
#print(response) 
#response = requests.get(myUrl, verify=True)
#print(json_data)


#v1 = client.CoreV1Api()

#v1.list_node()


#pod_logs = v1.read_namespaced_pod_log(name = 'testpod', container = 'testpod', namespace='interview', follow=False)
#pod_logs = v1.read_namespaced_pod_log(name = 'demo-hello-world-es-86bc79b9c8-5z8n5', container = 'demo-hello-world-es', namespace='interview', follow=False)

#print("hello worls")
#v1.list_namespaced_pod(namespace='interview')
#pods =  v1.list_namespaced_pod(namespace='interview')
#print(pods)
#print("printing pod-logs")
#print(pod_logs)

