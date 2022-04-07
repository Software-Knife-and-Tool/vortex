#!/bin/bash

COUNTER=0
while true; do
    sudo -E ./circles.py;
    sudo -E ./display.py example.png;
    sleep 300;
    ((COUNTER++));
    if [ $((COUNTER % 6)) -eq 0 ]; then
      sudo -E ./clean.py > /dev/null;
    fi;
done
