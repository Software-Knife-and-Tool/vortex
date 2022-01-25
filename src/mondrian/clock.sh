#!/bin/bash

COUNTER=0
while true; do
    sudo ./circles.py;
    sudo ./display.py example.png;
    sleep 300;
    ((COUNTER++));
    if [ $((COUNTER % 6)) -eq 0 ]; then
      sudo ./clean.py > /dev/null;
    fi;
done
