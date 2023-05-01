#!/bin/bash
response=$(curl -s -w "%{http_code}" $1)
[ "$response" == 200 ] && curl -s $1
