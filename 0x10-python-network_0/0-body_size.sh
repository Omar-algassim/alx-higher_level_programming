#!/bin/bash
# count the byte of curl

curl -s "$1" | wc -c
