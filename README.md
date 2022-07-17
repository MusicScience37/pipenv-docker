# pipenv-docker

[![dockeri.co](https://dockeri.co/image/musicscience37/pipenv)](https://hub.docker.com/r/musicscience37/pipenv)

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/MusicScience37/pipenv-docker?label=latest)

[![pipeline status](https://gitlab.com/musicscience37/pipenv-docker/badges/develop/pipeline.svg)](https://gitlab.com/musicscience37/pipenv-docker/commits/develop)

Dockerfile to use pipenv in Docker container.

Container images contains the following tools:

- python3
- pyenv
- venv
- pipenv

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/musicscience37/pipenv-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37/pipenv-docker`
- [Docker Hub](https://hub.docker.com/r/musicscience37/pipenv)
  - latest stable image: `docker pull musicscience37/pipenv`

## Repositories

- [GitLab](https://gitlab.com/musicscience37/pipenv-docker):
  for development including CI
- [GitHub](https://github.com/MusicScience37/pipenv-docker):
  mirror repository

## Testing

For test of this project,
use `./tool.py test` command.
