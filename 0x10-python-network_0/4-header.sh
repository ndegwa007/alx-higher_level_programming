#!/bin/bash
#script takes in URL as an argument this time sets a header variable
curl -s $1 -H "X-School-User-Id: 98"
