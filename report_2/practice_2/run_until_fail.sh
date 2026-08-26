#!/bin/bash
count=0
while true; do
    ((count++))
    ./test.sh > stdout.log 2> stderr.log
    if [ $? -ne 0 ]; then
        echo "Failed after $count runs"
        break
    fi
done
