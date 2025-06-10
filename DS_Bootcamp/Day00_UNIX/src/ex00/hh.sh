#!/bin/sh

# Check if a job title is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <job_title>"
    exit 1
fi

# Get job title from arguments
JOB_TITLE="$1"

# URL encode the job title (replace spaces with %20)
ENCODED_TITLE=$(echo "$JOB_TITLE" | sed 's/ /%20/g')

# HeadHunter API URL with search parameters
API_URL="https://api.hh.ru/vacancies?text=$ENCODED_TITLE&per_page=20"

# Fetch job listings using curl and parse with jq to format the output
curl -s "$API_URL" | jq  > hh.json

# Confirm completion
echo "Job vacancies saved to hh.json"
