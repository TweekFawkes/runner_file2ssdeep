#!/bin/bash

# Update package list
apt-get update

# Install basic dependencies
apt-get install -y python3 python3-pip python-is-python3

# Install ssdeep system library (required for Python ssdeep package)
apt-get install -y libfuzzy-dev

# Install Python dependencies
pip install -r requirements.txt
