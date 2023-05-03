#!/bin/bash
# bash script that sends a post request to a passed url
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
