#!/bin/bash -e

cd $(dirname $0)

echo "> python version"
python --version

echo "> python3.x versions"
python3.10 --version
python3.11 --version
python3.12 --version
python3.13 --version

echo "> python shared library"
ls -l ~/.pyenv/versions/3.13.11/lib/libpython3.so

echo "> pipenv version"
pipenv --version

echo "> test pipenv"
rm -rf project
mkdir project
cd project
pipenv --python 3.13
pipenv install sphinx pylint pytest
