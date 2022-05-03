#!/user/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="newMac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
newMacAddy = options.newMac

print("[+] Changing MAC address for " + interface + " to " + newMacAddy)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw either", newMacAddy])
subprocess.call(["ifconfig", interface, "up"])



