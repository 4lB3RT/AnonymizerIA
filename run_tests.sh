#!/bin/bash

# Create tests directory if it doesn't exist
mkdir -p tests

# Install required packages
pip install requests

# Run the test script
python tests/test_database_generation.py 