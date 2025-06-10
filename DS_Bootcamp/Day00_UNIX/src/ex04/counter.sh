#!/bin/sh

# Input and output file names
INPUT_FILE="../ex03/hh_positions.csv"
OUTPUT_FILE="hh_uniq_positions.csv"

# Extract the 'name' column (excluding the header), count unique occurrences, and sort in descending order
tail -n +2 "$INPUT_FILE" | cut -d',' -f3 | sort | uniq -c | sort -nr | awk '{print "\""$2"\","$1}' > "$OUTPUT_FILE.tmp"

# Add header and merge with data
echo '"name","count"' > "$OUTPUT_FILE"
cat "$OUTPUT_FILE.tmp" >> "$OUTPUT_FILE"
rm "$OUTPUT_FILE.tmp"

# Ensure the script is executable
chmod +x counter.sh