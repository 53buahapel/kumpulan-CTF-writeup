## Judul Soal
exfiltrate 1

## Deskripsi Soal
Hacker exfiltrate some data

---
## Proof of Concept
- hacker exfiltrate data through icmp

## solve

1. saya menggunakan scapy untuk membaca pcap di python
2. berikut adalah script yang saya buat

```python
from scapy.all import *
import os

capture = rdpcap('a.pcap')
ping_data = b''

for i in range(0,1886,2):
    ping_data += capture[i].load[-32:-16]

pdf = open('flag.pdf', 'wb').write(ping_data)
os.system("xdg-open flag.pdf")
```
3. untuk flag nya ada di dalam pdf dan bewarna sama dengan backround, jadi untuk mengetahui flag nya saya drag seluruh tulisan dan copy paste ke dalam clipboard

## Flag

LKSSMK{icmp_exifiltrate_is_dope}