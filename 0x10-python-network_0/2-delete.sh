#!/bin/bash
# bash script that sends a deleter request to the URL passed as argument
curl -sX "$1" DELETE
