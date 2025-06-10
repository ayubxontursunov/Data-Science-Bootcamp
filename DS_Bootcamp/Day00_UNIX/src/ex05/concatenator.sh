#!/bin/sh

# Output file
OUTPUT_FILE="concatenated.csv"

# Get the first CSV file and extract header
HEADER=$(head -n 1 $(ls *.csv | head -n 1))

# Write header to output file
echo "$HEADER" > "$OUTPUT_FILE"

# Concatenate all partitioned files excluding their headers
tail -q -n +2 *.csv >> "$OUTPUT_FILE"

# Ensure the script is executable
chmod +x concatenator.sh
