#!/bin/bash -e

cd $(dirname $0)

echo "> python version"
python --version

echo "> python shared library"
ls -l ~/.pyenv/versions/3.9.13/lib/libpython3.so

echo "> pipenv version"
pipenv --version

echo "> test pipenv"
rm -rf project
mkdir project
cd project
pipenv install sphinx pylint pytest
