### Kubernetes Apps monitoring using python 

1. Metrics Server is installed using component.yaml file
```
kubectl create -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.7/components.yaml

added --kubelet-insecure-tls in args section of container.

```

2.  RBAC serviceaccount  is configures to authenticate metrics server and k8s apis  using  cluster-role.yaml

3. Request to metrics api can done using below command which is being used in python script to GET pods metrics. 

```
curl -X GET https://kubernetes.default.svc:443/apis/metrics.k8s.io/v1beta1/pods --header "Authorization: Bearer $TOKEN" --insecure

```

5. Pods status informtion is fetched from k8s api 

```
https://kubernetes.default.svc:443/api/v1/pods

```
4.  The monitoring consists of 2 python scripts . One pytohn-app/pyton-app-web-v3.py which periodically(every 2 secs) collects metrics and generates html file at /web/html/index.html. Second one runs a webserver litening on port 8000 of pod which is then exposed as service to access from outside k8s cluster. Both of these scripts are deloyed as containers in pod sharing same volumemount.
  

5. Docker files and requirements.txt  used for creating container images are placed inside folders python-app/ and web-server/.


  


