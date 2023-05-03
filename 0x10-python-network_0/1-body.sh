#!/bin/bash
#script that sends a GET request to a URL and displays only the body of the response with a 200 status code
curl -s -X "GET" $1 | sed -n '/^HTTP\/1.1 200 /, $p'
