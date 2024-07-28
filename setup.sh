#!/bin/bash

sudo apt update && sudo apt upgrade -y
brew update && brew upgrade

brew install gcc make sqlite python@3.12

# install this to link in the sqlite3 library (for minimail)
sudo apt-get install libsqlite3-dev

python3.12 -m venv env
source env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
