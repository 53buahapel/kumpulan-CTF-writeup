#!/bin/python3

from scapy.all import *
import os

capture = rdpcap('a.pcap')
ping_data = b''

for i in range(0,1886,2):
    ping_data += capture[i].load[-32:-16]

pdf = open('flag.pdf', 'wb').write(ping_data)
os.system("xdg-open flag.pdf")
