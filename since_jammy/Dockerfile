ARG IMAGE_TAG
FROM ubuntu:${IMAGE_TAG}

ENV LANG=C.UTF-8

RUN apt-get update && \
    # Prevent error due to intractive configuration of tzdata.
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    tzdata && \
    apt-get install -y --no-install-recommends \
    # Packages for pyenv
    # (Reference: https://github.com/pyenv/pyenv/wiki )
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    curl \
    git \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    libzstd-dev \
    llvm \
    # Packages for pipx, pipenv
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    # Pipx
    pipx \
    # Packages for development
    git \
    git-lfs \
    nano \
    wget \
    ca-certificates \
    && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

RUN pipx install pipenv && \
    pipx install poetry

ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="/root/.local/bin:${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"
WORKDIR /root
RUN wget -nv -O pyenv_install.bash https://pyenv.run && \
    bash pyenv_install.bash && \
    eval "$(pyenv init --path)" && \
    export PYTHON_CONFIGURE_OPTS="--enable-shared" && \
    pyenv install 3.11.15 && \
    pyenv install 3.12.13 && \
    pyenv install 3.13.13 && \
    pyenv install 3.14.5 && \
    pyenv global 3.13.13 3.14.5 3.12.13 3.11.15
