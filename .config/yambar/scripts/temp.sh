#!/bin/bash
/usr/bin/echo -n "temp|string|"
/usr/bin/sensors | /usr/bin/grep -Eo "Package id 0:  [+][0-9]+\.[0-9].." | /usr/bin/cut -d'+' -f2
echo ""