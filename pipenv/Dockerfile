FROM ubuntu:focal-20210416

ENV LANG=C.UTF-8

RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main" >> /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    python3-pip=20.0.2-5ubuntu1.5 \
    python3-dev=3.8.2-0ubuntu2 \
    python3-setuptools=45.2.0-1 \
    python3-wheel=0.34.2-1 \
    python3-venv=3.8.2-0ubuntu2 \
    git=1:2.25.1-1ubuntu3.1 \
    wget=1.20.3-1ubuntu1 \
    curl=7.68.0-1ubuntu2.5 \
    tzdata=2021a-0ubuntu0.20.04 && \
    apt-get build-dep -y --no-install-recommends \
    python3.8=3.8.5-1~20.04.3 && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="${PYENV_ROOT}/bin:${PATH}"
WORKDIR /root
RUN wget -nv https://github.com/pyenv/pyenv/archive/refs/tags/v2.0.1.tar.gz && \
    tar xf v2.0.1.tar.gz && \
    mv pyenv-2.0.1 .pyenv && \
    rm v2.0.1.tar.gz && \
    echo "eval \"$(pyenv init --path)\"" >> ~/.profile && \
    pip3 install --no-cache-dir pipenv==2021.5.29 && \
    eval "$(pyenv init -)" && \
    pyenv install 3.8.10 && \
    pyenv install 3.9.5 && \
    pyenv global 3.8.10
