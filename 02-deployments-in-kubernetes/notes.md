# Deployments in Kubernetes

## Erzeuge einen Service

### Mittels Manifests
Aus dem aktuellen Verzeichnis lautet der Befehl wie folgt:

```bash
kubectl create -f manifests/demo-svc.yaml
```

### Mittels *expose*

Auf einen Pod bezogen:

```bash
kubectl expose pod demo-pod --port=80 --target-port=8080 
```
Auf ein Deployment bezogen:

```bash
kubectl expose deployment demo-deploy --port=80 --target-port=8080 --type=NodePort
```

## Erzeuge einen Pod

### Mittels Manifests

Aus dem aktuellen Verzeichnis lautet der Befehl wie folgt:

```bash
kubectl create -f manifests/demo-pod.yaml
```

### Imperativ

Imperativ wird *run* verwendet:

```bash
kubectl run --generator=run-pod/v1 demo-pod --image=luksa/kubia:v4
```

## Replicasets

### Erzeuge ein Replicaset mittels Manifest

Hierfür wird *scale* verwendet:

```bash
kubectl scale replicaset demo-rs --replicas=5
```

Alternativ kann man das Replicaset entsprechend editieren:

```bash
kubectl edit replicaset demo-rs
```

### Skalieren eines Replicasets

Aus dem aktuellen Verzeichnis lautet der Befehl wie folgt:

```bash
kubectl create -f manifests/demo-rs.yaml
```

## Deployments

### Erzeuge ein Deployment mittels Manifest

Aus dem aktuellen Verzeichnis lautet der Befehl wie folgt:

```bash
kubectl create -f manifests/demo-pod.yaml
```

### Erzeuge ein Deployment imperativ

Imperativ wird ein Deployment wie folgt erzeugt:

```bash
kubectl create deployment imperativ-deployment --image=nginx
```

### Rollouts managen

Ein Update des Images kann wie folgt eingespielt werden:

```bash
kubectl set image deployment.v1.apps/demo-deploy kubia=luksa/kubia
```

Ein Update kann wie folgt zurückgenommen werden:

```bash
kubectl rollout undo deployment.v1.apps/demo-deploy
```