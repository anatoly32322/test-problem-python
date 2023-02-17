#!/bin/bash

echo '=====PYLINT====='
pylint ./config.py ./exceptions.py ./main.py ./solution.py ./utils.py ./test/*
echo '======MYPY======'
mypy ./config.py ./exceptions.py ./main.py ./solution.py ./utils.py ./test/*

echo '==[TESTING]=='
echo '====UNIT-TESTS===='
python -m unittest test/unit_test.py
