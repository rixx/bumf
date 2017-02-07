#!/bin/bash

set -e

if [ $TRAVIS_COMPONENT = "server" ]; then
    cd server
    pip install -r requirements.txt
    pip install -r requirements/development.txt
    isort -c -rc .
    pylama
    pytest --cov=bumf
    codecov
else
    cd web-client
    rm -rf ~/.nvm && git clone https://github.com/creationix/nvm.git ~/.nvm && (cd ~/.nvm && git checkout `git describe --abbrev=0 --tags`) && source ~/.nvm/nvm.sh && nvm install 7.5.0
    npm install --python=/usr/bin/python2
    npm run lint
fi
