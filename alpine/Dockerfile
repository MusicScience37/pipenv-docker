FROM alpine

ENV LANG=C.UTF-8

RUN apk add --no-cache \
    # Packages for pyenv
    # (Reference: https://github.com/pyenv/pyenv/wiki )
    git \
    bash \
    build-base \
    libffi-dev \
    openssl-dev \
    bzip2-dev \
    zlib-dev \
    xz-dev \
    readline-dev \
    sqlite-dev \
    tk-dev \
    # Packages for pipenv, poetry.
    pipx \
    # Additional packages for development.
    git-lfs \
    wget \
    curl \
    make \
    gcc \
    g++ \
    nano

RUN pipx install pipenv poetry

ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="/root/.local/bin:${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"
WORKDIR /root
RUN wget -nv -O pyenv_install.bash https://pyenv.run && \
    bash pyenv_install.bash && \
    eval "$(pyenv init --path)" && \
    export PYTHON_CONFIGURE_OPTS="--enable-shared" && \
    pyenv install 3.9.21 && \
    pyenv install 3.10.16 && \
    pyenv install 3.11.11 && \
    pyenv install 3.12.9 && \
    pyenv install 3.13.2 && \
    pyenv global 3.12.9 3.13.2 3.11.11 3.10.16 3.9.21
