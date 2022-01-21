#/bin/bash
cycles=0
while true
do
  sudo ./vortex-clock.py > /dev/null
  sleep 300
  ((cycles=cycles+1))
  if [ $((cycles % 6)) -eq 0 ]
  then
      sudo ./clean.py > /dev/null
  fi
done
