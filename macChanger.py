#!/user/bin/env python

import subprocess
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface. Use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify a mac address. Use --help for more information.")
    return options


def mac_changer(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw either", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_args()
# mac_changer(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
