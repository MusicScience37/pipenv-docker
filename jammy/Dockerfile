FROM ubuntu:jammy-20220531

ENV LANG=C.UTF-8

RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ jammy main" >> /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    tzdata=2022a-0ubuntu1 && \
    apt-get install -y --no-install-recommends \
    # Packages for pyenv
    # (Reference: https://github.com/pyenv/pyenv/wiki )
    make=4.3-4.1build1 \
    build-essential=12.9ubuntu3 \
    libssl-dev=3.0.2-0ubuntu1.6 \
    zlib1g-dev=1:1.2.11.dfsg-2ubuntu9 \
    libbz2-dev=1.0.8-5build1 \
    libreadline-dev=8.1.2-1 \
    libsqlite3-dev=3.37.2-2 \
    wget=1.21.2-2ubuntu1 \
    curl=7.81.0-1ubuntu1.3 \
    llvm=1:14.0-55~exp2 \
    libncursesw5-dev=6.3-2 \
    xz-utils=5.2.5-2ubuntu1 \
    tk-dev=8.6.11+1build2 \
    libxml2-dev=2.9.13+dfsg-1ubuntu0.1 \
    libxmlsec1-dev=1.2.33-1build2 \
    libffi-dev=3.4.2-4 \
    liblzma-dev=5.2.5-2ubuntu1 \
    # Packages for pipx
    python3-pip=22.0.2+dfsg-1 \
    python3-dev=3.10.4-0ubuntu2 \
    python3-setuptools=59.6.0-1.2 \
    python3-wheel=0.37.1-2 \
    python3-venv=3.10.4-0ubuntu2 \
    # Packages for development
    git=1:2.34.1-1ubuntu1.2 \
    nano=6.2-1 && \
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
