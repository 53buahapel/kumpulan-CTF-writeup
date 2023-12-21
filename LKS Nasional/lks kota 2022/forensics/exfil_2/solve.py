#!/bin/python3

from os import system

system('tshark -r traffic.pcap -T fields -e dns.qry.name -Y "dns.qry.name contains hackmeifyoucan.space" > dump.txt')

file = open('dump.txt', 'r').readlines()
flag = ""

for i in range(0,len(file),3):
	flag += file[i][:32]

flag = flag.removesuffix('.hackmeifyoucan.')
flag = bytes.fromhex(flag)
jfif = open('flag.jfif', 'wb').write(flag)
system('xdg-open flag.jfif')