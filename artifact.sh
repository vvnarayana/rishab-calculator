#!/bin/bash
cd /home/circleci/Flask-calculator
zip -r /home/circleci/Flask-calculator/Flask-calculator.zip /home/circleci/Flask-calculator/*
chmod 777 Flask-calculator.zip
cp /home/circleci/Flask-calculator/Flask-calculator.zip /home/circleci/
ls -la
pwd
