#!/bin/bash -e

cd $(dirname $0)

echo "> python version"
python --version

echo "> python shared library"
ls -l ~/.pyenv/versions/3.10.8/lib/libpython3.so

echo "> pipenv version"
pipenv --version

echo "> test pipenv"
rm -rf project
mkdir project
cd project
pipenv --python 3.10
pipenv install sphinx pylint pytest
