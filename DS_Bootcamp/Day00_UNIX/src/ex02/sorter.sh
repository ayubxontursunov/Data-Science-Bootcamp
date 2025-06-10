#!/bin/sh

# Check if hh.csv exists
if [ ! -f "../ex01/hh.csv" ]; then
    echo "Error: hh.csv file not found in ex01 folder."
    exit 1
fi

# Extract the header (first row) from hh.csv
head -n 1 ../ex01/hh.csv > hh_sorted.csv

# Sort the rest of the file based on "created_at" (column 2) and "id" (column 1)
# The sort command uses -t to specify the delimiter (,) and -k to specify the sorting keys
# -k2,2 sorts by the "created_at" column and -k1,1 sorts by the "id" column
tail -n +2 ../ex01/hh.csv | sort -t, -k2,2 -k1,1 >> hh_sorted.csv


echo "CSV file sorted and saved as hh_sorted.csv"
