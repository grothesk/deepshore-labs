#!/usr/bin/env bash
# Bedingt durch Dockerfile...
cd ..

# Build - Tags entsprechen <repo>:<tag> im Register
docker image build -f docker/Dockerfile -t grothesk/deeptalk-app:1.0.0 -t grothesk/deeptalk-app:latest .

# Login - Anmeldung beim Register
docker login -u "$DOCKER_REGISTRY_USER" -p "$DOCKER_REGISTRY_PASSWORD"

# Push - Upload der Images
docker image push grothesk/deeptalk-app:latest
docker image push grothesk/deeptalk-app:1.0.0
