#!/bin/bash

# Path to the zip file
ZIP_FILE="/home/simmonsc/goinfre/ml-25m.zip"

# Check if the zip file exists
if [ -f "$ZIP_FILE" ]; then
    echo "Unzipping $ZIP_FILE..."

    # Change directory to the folder where the zip file is located
    cd /home/simmonsc/goinfre/

    # Unzip the file
    unzip -q "$ZIP_FILE"  # -q is for quiet mode, suppressing the output

    echo "Unzip completed."
else
    echo "Zip file not found at $ZIP_FILE"
fi
