#!/bin/bash
# bash script that takes the URL and & displays only the status code
curl -so /dev/null -w '%{http_code}' "$1"
