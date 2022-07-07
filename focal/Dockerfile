FROM ubuntu:focal-20220531

ENV LANG=C.UTF-8

RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main" >> /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    tzdata=2022a-0ubuntu0.20.04 && \
    apt-get install -y --no-install-recommends \
    # Packages for pyenv
    # (Reference: https://github.com/pyenv/pyenv/wiki )
    make=4.2.1-1.2 \
    build-essential=12.8ubuntu1.1 \
    libssl-dev=1.1.1f-1ubuntu2.16 \
    zlib1g-dev=1:1.2.11.dfsg-2ubuntu1.3 \
    libbz2-dev=1.0.8-2 \
    libreadline-dev=8.0-4 \
    libsqlite3-dev=3.31.1-4ubuntu0.3 \
    wget=1.20.3-1ubuntu2 \
    curl=7.68.0-1ubuntu2.12 \
    llvm=1:10.0-50~exp1 \
    libncursesw5-dev=6.2-0ubuntu2 \
    xz-utils=5.2.4-1ubuntu1.1 \
    tk-dev=8.6.9+1 \
    libxml2-dev=2.9.10+dfsg-5ubuntu0.20.04.3 \
    libxmlsec1-dev=1.2.28-2 \
    libffi-dev=3.3-4 \
    liblzma-dev=5.2.4-1ubuntu1.1 \
    # Packages for pipx
    python3-pip=20.0.2-5ubuntu1.6 \
    python3-dev=3.8.2-0ubuntu2 \
    python3-setuptools=45.2.0-1 \
    python3-wheel=0.34.2-1 \
    python3-venv=3.8.2-0ubuntu2 \
    # Packages for development
    git=1:2.25.1-1ubuntu3.4 \
    nano=4.8-1ubuntu1 && \
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
