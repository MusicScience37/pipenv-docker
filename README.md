# pipenv-docker

[![pipeline status](https://gitlab.com/MusicScience37Projects/docker/pipenv-docker/badges/main/pipeline.svg)](https://gitlab.com/MusicScience37Projects/docker/pipenv-docker/-/commits/main)
![Docker Pulls](https://img.shields.io/docker/pulls/musicscience37/pipenv)
![Docker Image Size (tag)](https://img.shields.io/docker/image-size/musicscience37/pipenv/latest)

Dockerfile to use pipenv in Docker container.

Container images contains the following tools:

- python3
- pyenv
- venv
- pipenv
- poetry

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/MusicScience37Projects/docker/pipenv-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37projects/docker/pipenv-docker`
- [Docker Hub](https://hub.docker.com/r/musicscience37/pipenv)
  - latest stable image: `docker pull musicscience37/pipenv`

## Repositories

- [GitLab](https://gitlab.com/MusicScience37Projects/docker/pipenv-docker):
  for development including CI
- [GitHub](https://github.com/MusicScience37/pipenv-docker):
  mirror repository

## Testing

For test of this project,
use `./tool.py test` command.
