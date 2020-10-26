# pipenv-docker

[![dockeri.co](https://dockeri.co/image/musicscience37/pipenv)](https://hub.docker.com/r/musicscience37/pipenv)

![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/musicscience37/pipenv)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/musicscience37/pipenv)

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/MusicScience37/pipenv-docker?label=latest)

[![pipeline status](https://gitlab.com/musicscience37_ci/pipenv-docker/badges/develop/pipeline.svg)](https://gitlab.com/musicscience37_ci/pipenv-docker/commits/develop)

Dockerfile to use pipenv in Docker container.

Container images contains the following tools:

- python3
- pyenv
- venv
- pipenv

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/musicscience37_ci/pipenv-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37_ci/pipenv-docker`
- [Docker Hub](https://hub.docker.com/r/musicscience37/pipenv)
  - latest stable image: `docker pull musicscience37/pipenv`

## Repositories

- [GitLab](https://gitlab.com/musicscience37_ci/pipenv-docker):
  for development including CI
- [GitHub](https://github.com/MusicScience37/pipenv-docker):
  mirror repository for use in Docker Hub

## Testing

For test of this project,
execute `./run_test.sh` script.
