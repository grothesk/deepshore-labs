# DEEPTALK III
## Conditions
Environmentvariables must be set with credentials of DockerHub:
1. $DOCKER_REGISTRY_USER
2. $DOCKER_REGISTRY_PASSWORD
3. $DOCKER_REGISTRY
## Commands
### Start local services
#### Start influxdb
 ```bash
systemctl start influxdb

influxdb    (Start service)

influx  (Connect to influx)

```

 ```bash
systemctl start grafana-server

systemctl status grafana-server

```

 ```bash
pip3 install -r requirements.txt

cd app

export PYTHONPATH=/home/frederic/Code/Deeptalk/deeptalk-app/app

python3 app/main.py

```


### Build Docker Image
 ```bash
docker build -f dockerfiles/Dockerfile -t flask_app .
```

### Run Docker Image
```bash
docker run -d -p 8000:80 flask_app
```

### Docker-Compose
```bash
docker-compose -f docker/docker-compose.yml build 
```

### Create DB
```bash
curl -i -X POST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE deeptalk"
```

### Generate Datapoints
```bash
$ curl -X POST http://localhost:8080/generator -d "@data.json" -H 'Content-type: application/json'
```
