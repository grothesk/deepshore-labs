# Einstieg in Kubernetes mit Minikube - Befehle

## Container (Docker)

Hinweise zur Installation von Docker können hier abgerufen werden: 
[Get Docker](https://docs.docker.com/get-docker/)

Starte einen Redis-Container in Docker:

```bash
docker run -p 6379:6379 -it redis
```

Optionen:
- **-p 6379:6379** : richte Port-Mapping mit port_host:port_container ein
- **-it** : starte im interaktiven Modus

Starte redis-cli:

```bash
redis-cli
```

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