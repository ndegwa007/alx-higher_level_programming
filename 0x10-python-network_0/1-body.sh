#!/bin/bash
# Sends a GET request to a URL and returns the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}\n%{body}" -L $1 | awk 'BEGIN {RS="\n\n|\r\n\r\n"} ; {if ($1 == "200") print $2}'
