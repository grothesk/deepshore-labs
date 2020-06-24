#!/usr/bin/env bash
cd ..
# Build - Tags entsprechen <repo>:<version> im Register
docker build -f docker/Dockerfile -t grothesk/deeptalk-app:1.0.0 -t grothesk/deeptalk-app:latest .
# Login
docker login -u "$DOCKER_REGISTRY_USER" -p "$DOCKER_REGISTRY_PASSWORD" $DOCKER_REGISTRY
# Push
docker push grothesk/deeptalk-app:latest
docker push grothesk/deeptalk-app:1.0.0
