#!/bin/bash -e

cd $(dirname $0)

echo "> python version"
python --version

echo "> python3.x versions"
python3.9 --version
python3.10 --version
python3.11 --version
python3.12 --version

echo "> python shared library"
ls -l ~/.pyenv/versions/3.12.6/lib/libpython3.so

echo "> pipenv version"
pipenv --version

echo "> test pipenv"
rm -rf project
mkdir project
cd project
pipenv --python 3.12
pipenv install sphinx pylint pytest
