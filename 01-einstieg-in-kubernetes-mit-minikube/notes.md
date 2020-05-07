# Einstieg in Kubernetes mit Minikube

## Container (Docker)

Hinweise zur Installation von Docker können hier abgerufen werden: 
[Get Docker](https://docs.docker.com/get-docker/)

Starte einen Redis-Container in Docker:

```bash
docker run -p 6379:6379 -it redis
```

Optionen:
- **-p 6379:6379** : richte ein Port-Mapping mit port_host:port_container ein
- **-it** : starte den Container im interaktiven Modus

Starte redis-cli:

```bash
redis-cli
```

## kubectl

Hinweise zur Installation von kubectl können hier abgerufen werden: 
[Install kubectl](https://kubernetes.io/de/docs/tasks/tools/install-kubectl/)

## Minikube

Hinweise zur Installation von Minikube können hier abgerufen werden: 
[Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

Starte einen Minikube-Cluster:

```bash
minikube start -p lab --vm-driver=virtualbox
```

Optionen:
- -p lab : Profilname ist lab
- --vm-driver=virtualbox : verwende Virtualbox zur Virtualisierung
