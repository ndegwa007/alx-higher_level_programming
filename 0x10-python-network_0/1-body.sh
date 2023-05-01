#!/bin/bash
# script takes in URL, sends a GET request to the URL and displays the body of the response
[ $(curl -s -w "%{http_code}" $1) == "200" ] && curl -s $1
