#!/bin/sh

# Input and output file names
INPUT_FILE="../ex02/hh_sorted.csv"
OUTPUT_FILE="hh_positions.csv"

# Extract header
head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"

# Process the file excluding the header
tail -n +2 "$INPUT_FILE" | awk -F',' '{
    name = $3;
    position="-";
    if (name ~ /Junior/) position="Junior";
    if (name ~ /Middle/) position=(position == "-" ? "Middle" : position "/Middle");
    if (name ~ /Senior/) position=(position == "-" ? "Senior" : position "/Senior");
    print $1","$2","position","$4","$5;
}' OFS="," >> "$OUTPUT_FILE"

# Ensure the script is executable
chmod +x cleaner.sh