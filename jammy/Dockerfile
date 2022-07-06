FROM ubuntu:jammy-20220531

ENV LANG=C.UTF-8

RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ jammy main" >> /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    tzdata=2022a-0ubuntu1 && \
    apt-get build-dep -y --no-install-recommends \
    python3.10=3.10.4-3 && \
    apt-get install -y --no-install-recommends \
    python3-pip=22.0.2+dfsg-1 \
    python3-dev=3.10.4-0ubuntu2 \
    python3-setuptools=59.6.0-1.2 \
    python3-wheel=0.37.1-2 \
    python3-venv=3.10.4-0ubuntu2 \
    git=1:2.34.1-1ubuntu1.2 \
    wget=1.21.2-2ubuntu1 \
    curl=7.81.0-1ubuntu1.3 && \
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
    pyenv install 3.9.13 && \
    pyenv install 3.10.5 && \
    pip3 install --no-cache-dir pipx==1.1.0 && \
    pipx install pipenv==2022.7.4 && \
    pyenv global 3.9.13
