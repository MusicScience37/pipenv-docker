FROM ubuntu:jammy-20220130

ENV LANG=C.UTF-8

RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ jammy main" >> /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    tzdata=2021e-1ubuntu1 && \
    apt-get build-dep -y --no-install-recommends \
    python3.9=3.9.10-1 && \
    apt-get install -y --no-install-recommends \
    python3-pip=22.0.2+dfsg-1 \
    python3-dev=3.9.7-4 \
    python3-setuptools=59.6.0-1.2 \
    python3-wheel=0.37.1-2 \
    python3-venv=3.9.7-4 \
    git=1:2.34.1-1ubuntu1 \
    wget=1.21.2-2ubuntu1 \
    curl=7.81.0-1 && \
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
    pyenv install 3.9.10 && \
    pip3 install --no-cache-dir pipx==1.0.0 && \
    pipx install pipenv==2022.1.8 && \
    pyenv global 3.9.10
