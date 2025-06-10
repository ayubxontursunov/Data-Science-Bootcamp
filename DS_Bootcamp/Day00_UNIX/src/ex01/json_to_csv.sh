#!/bin/sh

# Check if hh.json exists in the ex00 directory
if [ ! -f "../ex00/hh.json" ]; then
    echo "Error: hh.json file not found in ex00 folder."
    exit 1
fi

# Execute jq filter and convert the result to CSV
# Add headers manually to the CSV file
echo "id,created_at,name,has_test,alternate_url" > hh.csv

# Apply the jq filter, format as CSV and append to hh.csv
jq -r '.items[] | [.id, .created_at, .name, .has_test, .alternate_url] | @csv' ../ex00/hh.json >> hh.csv

# Confirm completion
echo "CSV file created: hh.csv"












#!/bin/sh


if [ ! -f "../ex00/hh.json" ]; then
    echo "Error: hh.json file not found in ex00 folder."
    exit 1
fi


echo "id,created_at,name,has_test,alternate_url" > hh.csv


jq -r '.items[] | [.id, .created_at, .name, .has_test, .alternate_url] | @csv' ../ex00/hh.json >> hh.csv

