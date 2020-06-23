#!/usr/bin/env bash
kubectl create configmap deeptalk-app --from-literal=INFLUX_HOST=influxdb
kubectl create configmap influxdb --from-literal=INFLUXDB_DB=deeptalk
kubectl create configmap grafana --from-file=datasource.yml=grafana_config/datasource.yml --from-file=dashboard.json=grafana_config/dashboard.json --from-file=dashboard-providers.yml=grafana_config/dashboard-providers.yml
