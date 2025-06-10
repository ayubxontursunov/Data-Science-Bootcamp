#!/bin/sh

# Input file
INPUT_FILE="../ex03/hh_positions.csv"

# Extract header
HEADER=$(head -n 1 "$INPUT_FILE")

# Process file excluding the header
tail -n +2 "$INPUT_FILE" | while IFS=, read -r id created_at name has_test alternate_url; do
    # Extract date part (YYYY-MM-DD) from created_at
    date_part=$(echo "$created_at" | cut -d'T' -f1)
    
    # Define output file
    OUTPUT_FILE="$date_part.csv"
    
    # If file does not exist, create it with a header
    if [ ! -f "$OUTPUT_FILE" ]; then
        echo "$HEADER" > "$OUTPUT_FILE"
    fi
    
    # Append row to the respective partition file
    echo "$id,$created_at,$name,$has_test,$alternate_url" >> "$OUTPUT_FILE"
done

# Ensure the script is executable
chmod +x partitioner.sh
