#!/bin/bash

export DEST_JSON='database_empty.json' 
python -m pytest -vv test_handler_empty_database.py 

export DEST_JSON='database.json' 
python -m pytest  test_handler.py 
