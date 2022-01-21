#/bin/bash
while true; do
  sudo ./orb-clock.py > /dev/null;
  sleep 300
  sudo ./clean.py > /dev/null
done
