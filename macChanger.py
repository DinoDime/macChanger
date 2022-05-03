#!/user/bin/env python

import subprocess
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def mac_changer(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw either", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


(options, arguments) = get_args()
mac_changer(options.interface, options.new_mac)