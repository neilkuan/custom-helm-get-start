
## Example for helm chart getting start.

```bash
$ helm create pychart
```

### Docker build flow
```bash
$ docker build -t $reponame/$imagename:$tag .
```

### Docker local testing
```bash
$ docker run -it --rm $reponame/$imagename:$tag
```

## Example helm install chart
```bash
# $ helm install <name you want> ./<helm chart dir name>
$ helm install py ./pychart
$ helm upgrade py ./pychartRelease "py" has been upgraded. Happy Helming!
NAME: py
LAST DEPLOYED: Wed Dec  9 17:49:14 2020
NAMESPACE: default
STATUS: deployed
REVISION: 2
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=pychart,app.kubernetes.io/instance=py" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:80
```

see more [helm docs](https://helm.sh/docs/helm/helm_install/) 