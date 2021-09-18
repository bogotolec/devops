# Kubernetes

This file contains report of what have I done for lab 9.

## Output of `kubectl get pods,svc` (first time)

```
NAME                          READY   STATUS    RESTARTS   AGE
pod/devops-64857c778d-6nqb4   1/1     Running   0          2m50s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/devops       LoadBalancer   10.108.245.64   127.0.0.1     8888:30117/TCP   116s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          7m18s
```

## Output of `kubectl get pods,svc` (second time)

```
NAME                                             READY   STATUS    RESTARTS   AGE
pod/devops-web-app-deployment-7f644dfbf5-rsd8f   1/1     Running   0          40s
pod/devops-web-app-deployment-7f644dfbf5-sbbgs   1/1     Running   0          39s
pod/devops-web-app-deployment-7f644dfbf5-zvrt9   1/1     Running   0          39s

NAME                             TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/devops-web-app-service   LoadBalancer   10.110.175.7   127.0.0.1     8888:30211/TCP   34s
service/kubernetes               ClusterIP      10.96.0.1      <none>        443/TCP          26m
```

## Output of `kubectl get pods,svc` (lab 10)

```
NAME                                             READY   STATUS    RESTARTS   AGE
pod/devops-web-app-6fbffc69cb-756qh              1/1     Running   0          4m3s
pod/devops-web-app-deployment-7f644dfbf5-rsd8f   1/1     Running   0          35m
pod/devops-web-app-deployment-7f644dfbf5-sbbgs   1/1     Running   0          34m
pod/devops-web-app-deployment-7f644dfbf5-zvrt9   1/1     Running   0          34m

NAME                             TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/devops-web-app           ClusterIP      10.110.13.252   <none>        8888/TCP         4m3s
service/devops-web-app-service   LoadBalancer   10.110.175.7    127.0.0.1     8888:30211/TCP   34m
service/kubernetes               ClusterIP      10.96.0.1       <none>        443/TCP          60m
```
