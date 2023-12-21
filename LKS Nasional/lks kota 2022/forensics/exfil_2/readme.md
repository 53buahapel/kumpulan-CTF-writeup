## Judul Soal
exfiltrate 2

## Deskripsi Soal
Hacker exfiltrate data, again ?

---
## Proof of Concept
- hacker exfiltrate data from the server through dns

## solve

1. saya menggunakan tshark untuk melakukan filter
2. berikut adalah script yang saya buat

```python
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
```

3. untuk flag nya berada dalam format  [jfif](flag.jfif)


## Flag

LKSSMK{w0w_dns_exifiltrate_is_really_common}