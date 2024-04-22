#!/bin/bash
echo "action|string|~/.config/sway/scripts/sway-sensible-terminal --title '__calendar__' -e bash -c '~/.config/yambar/scripts/vpn.sh'"
ip link show up type wireguard 2> /dev/null | grep '.' &> /dev/null && echo "type|string|wireguard" && echo "icon|string| " && echo "" && exit 0 
ip link show up type tun       2> /dev/null | grep '.' &> /dev/null && echo "type|string|openvpn" && echo "icon|string| " && echo "" && exit 0
echo "type|string|none"
echo "icon|string| "
echo ""
