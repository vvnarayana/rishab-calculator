#!/bin/bash
python -m venv antenv
source antenv/bin/activate
python -m pip install --upgrade pip
pip install setup
pip install pytest
pwd
pip install -r requirements.txt
