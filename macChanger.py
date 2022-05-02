#!/user/bin/env python

import subprocess

interface = input("Which interface's MAC address would you like changed?")
newMacAddy = input("What would you like the new MAC address to be?")

print("[+] Changing MAC address for " + interface + " to " + newMacAddy)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw either", newMacAddy])
subprocess.call(["ifconfig", interface, "up"])



