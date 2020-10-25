#!/bin/bash

cd $(dirname $0)

echo "> python version"
python --version

echo "> pipenv version"
pipenv --version

echo "> test pipenv"
mkdir project
cd project
pipenv install sphinx pylint pytest
