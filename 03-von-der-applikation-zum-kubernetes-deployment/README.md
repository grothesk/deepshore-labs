# DEEPTALK III
## Conditions
Environmentvariables must be set with credentials of DockerHub:
1. $DOCKER_REGISTRY_USER
2. $DOCKER_REGISTRY_PASSWORD
3. $DOCKER_REGISTRY

## Commands
### Local Setup
Following steps can be executed to 
#### Install Services
* [influxdb](https://www.influxdata.com/get-influxdb/)
* [Grafana](https://grafana.com/grafana/download)

#### Start influxdb
 
 ```bash
systemctl start influxdb
```
or

 ```bash
sudo influxd    (Start Srvice)

influx          (Connect Client)
```

#### Start grafana
 ```bash
systemctl start grafana-server
```
>**Note:** Check status of system with `systemctl status <service-name>`

#### Start Flask-App
 ```bash
pip3 install -r requirements.txt

cd app

export PYTHONPATH=/path/to/03-von-der-applikation-zum-kubernetes-deployment/app

python3 app/main.py
```
>**Note:** `PYTHONPATH` must be set accordingly

### Docker Setup
#### Build Docker Image
 ```bash
docker build -f docker/Dockerfile -t deeptalk_app .
```

#### Run Docker Image
```bash
docker run -d -p 8000:80 deeptalk_app
```

#### Run docker-compose
```bash
docker-compose -f docker/docker-compose.yml build

docker-compose -f docker/docker-compose.yml up
```

### Create DB
```bash
curl -i -X POST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE deeptalk"
```
or
```bash
influx

create database deeptalk
```
>**Note:** requires running influxdb

### Generate Datapoints
In order generate data send cURL POST request to `/generator`-endpoint:
```bash
$ curl -X POST http://localhost:8080/generator -d "@data.json" -H 'Content-type: application/json'
```
