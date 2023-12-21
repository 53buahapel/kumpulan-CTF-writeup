import hashlib

dns = open('./dnsmasq-ip-extract-dnsmasq.log', 'r').readlines()
a = []
for i in range(0,len(dns),3):
    a.append(dns[i][61:])

for i in range(len(a)):
    a[i] = a[i].strip()
    a[i] += " " + hashlib.sha256(a[i].encode()).hexdigest() + "\n"

for i in a:
    open('output.txt', 'a').write(i)
