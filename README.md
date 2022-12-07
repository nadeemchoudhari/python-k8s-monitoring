### Kubernetes Apps monitoring using python 

1. Metrics Server is installed using component.yaml file
```
kubectl create -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.7/components.yaml

added --kubelet-insecure-tls in args section of container.

```

2.  RBAC serviceaccount  is configures to access metrics cluster and resources using cluster-role.yaml

3. Request to metrics api can done using below command which is being used in python script to GET pods metrics. 

```
curl -X GET https://kubernetes.docker.internal:6443/apis/metrics.k8s.io/v1beta1/pods --header "Authorization: Bearer $TOKEN" --insecure

```

4. pod-usage.py is the python script which can be run as job in kubernetes clusters which will get cpu and mem usage of a pods running in all namespaces.

5. pod-usage-web.py is a script which implements the same but also publishes the information on  http server running on port 8000

