#!/bin/bash
# bash script that takes the URL and displays the size of the body
curl -s "$1" | wc -c
