
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


### [Rewrite Target](https://kubernetes.github.io/ingress-nginx/examples/rewrite/) 
> **Attention**
> Starting in Version 0.22.0, ingress definitions using the annotation nginx.ingress.kubernetes.io/rewrite-target are not backwards compatible with previous versions. In Version 0.22.0 and beyond, any substrings within the request URI that need to be passed to the rewritten path must explicitly be defined in a capture group.

> **Note**
> Captured groups are saved in numbered placeholders, chronologically, in the form $1, $2 ... $n. These placeholders can be used as parameters in the rewrite-target annotation.

Create an Ingress rule with a rewrite annotation:
```bash
$ echo '
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
  name: rewrite
  namespace: default
spec:
  rules:
  - host: rewrite.bar.com
    http:
      paths:
      - backend:
          serviceName: http-svc
          servicePort: 80
        path: /something(/|$)(.*)
' | kubectl create -f -
```
In this ingress definition, any characters captured by (.*) will be assigned to the placeholder $2, which is then used as a parameter in the rewrite-target annotation.

For example, the ingress definition above will result in the following rewrites:

- rewrite.bar.com/something rewrites to rewrite.bar.com/
- rewrite.bar.com/something/ rewrites to rewrite.bar.com/
- rewrite.bar.com/something/new rewrites to rewrite.bar.com/new