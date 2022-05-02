#!/user/bin/env python

import subprocess

interface = "wlan0"
newMacAddy = "00:11:22:33:44:77"

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw either " + newMacAddy, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

