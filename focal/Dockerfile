FROM ubuntu:focal-20220426

ENV LANG=C.UTF-8

RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main" >> /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    tzdata=2022a-0ubuntu0.20.04 && \
    apt-get build-dep -y --no-install-recommends \
    python3.8=3.8.10-0ubuntu1~20.04.4 && \
    apt-get install -y --no-install-recommends \
    python3-pip=20.0.2-5ubuntu1.6 \
    python3-dev=3.8.2-0ubuntu2 \
    python3-setuptools=45.2.0-1 \
    python3-wheel=0.34.2-1 \
    python3-venv=3.8.2-0ubuntu2 \
    git=1:2.25.1-1ubuntu3.4 \
    wget=1.20.3-1ubuntu2 \
    curl=7.68.0-1ubuntu2.11 && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="/root/.local/bin:${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"
WORKDIR /root
RUN wget -nv -O pyenv_install.bash https://pyenv.run && \
    bash pyenv_install.bash && \
    eval "$(pyenv init --path)" && \
    export PYTHON_CONFIGURE_OPTS="--enable-shared" && \
    pyenv install 3.9.12 && \
    pip3 install --no-cache-dir pipx==1.0.0 && \
    pipx install pipenv==2022.5.2 && \
    pyenv global 3.9.12
