#!/bin/bash
phases=(eclipse.png  phase-0.png  phase-1.png  phase-2.png  phase-3.png  phase-4.png  phase-5.png  phase-6.png	phase-7.png)
while true; do
    for ((phase=0;phase<${#phases[@]};phase++)); do
        sudo ./clock.py ./phases/${phases[phase]} > /dev/null;
        sleep 400
        sudo ./clean.py > /dev/null
    done
done
