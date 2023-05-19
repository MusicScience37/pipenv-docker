#!/bin/bash -e

cd $(dirname $0)

echo "> python version"
python --version

echo "> python3.x versions"
python3.8 --version
python3.9 --version
python3.10 --version
python3.11 --version

echo "> python shared library"
ls -l ~/.pyenv/versions/3.10.11/lib/libpython3.so

echo "> pipenv version"
pipenv --version

echo "> test pipenv"
rm -rf project
mkdir project
cd project
pipenv --python 3.10
pipenv install sphinx pylint pytest
