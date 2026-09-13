#!/bin/bash
for f in $(ls *.txt); do
  echo $f
done
if [ $1 == "hello" ]; then
  echo "hi"
fi
