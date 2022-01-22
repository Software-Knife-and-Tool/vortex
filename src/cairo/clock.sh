#!/bin/bash

COUNTER=0
while true; do
    ./kandinsky.py;
    sudo ./display.py example.png;
    sleep 300;
    ((COUNTER++));
    if [ $((COUNTER % 6)) -eq 0 ]; then
      sudo ./clean.py > /dev/null;
    fi;
done
