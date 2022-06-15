#!/usr/bin/python

import subprocess
import re
import sys

if len(sys.argv) != 2:
    print "\n[*] Usage: python " + sys.argv[0] + "<ip-address>\n"
    sys.exit(1)

def return_ttl(addr):
    proc = subprocess.Popen(["ping -c 1 %s" % addr, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.split()
    out = re.findall(r"\d{1,3}", out[12])
    
    return out[0]

def return_ttl_os_name(ttl_number):

    if ttl_number >= 0 and ttl_number <= 64:
            return "Linux"
    elif ttl_number >= 65 and ttl_number <= 128:
            return "Windows"
    else:
        return "Unknwon"    

if __name__ == '__main__´:
    addr = sys.argv[1]
    ttl = return_ttl(addr)

    try:    
            print"\n%s -> %s" % (addr, return_ttl_os_name(int(ttl)))

    except:
            pass
