#!/bin/bash
dunstctl set-paused true
if ([[ $(date +%T) > "20:00:00" ]] || [[ $(date +%T) < "10:00:00" ]])
then
    ln -fs ~/.config/sway/lock_night.png ~/.config/sway/lock.png
else
    ln -fs ~/.config/sway/lock_day.png ~/.config/sway/lock.png
fi
hyprlock
while pgrep -c hyprlock &> /dev/null
do
    sleep 5
done
dunstctl set-paused false