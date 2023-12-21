# dnsmasq-ip-extract

## Challenge Text
* Extract all **unique** IPs from `dnsmasq-ip-extract-dnsmasq.log`, hash each IP (SHA256), and write the IP + hash to a text file (IP and hash should be separated by a space, and each IP + hash entry should be on a new line).

    **NOTE:** Alphabetical characters in the hash should be lower case, as seen in example below. Otherwise, your flag will be incorrect!

* Example of text file output contents:
    ```
    10.59.78.165 a6dd519bf8c7c50df5ae519963b5cf1590a471f88343c603168645ff335b26fe
    10.244.220.245 20657ea410e8dd2dbf979a12fea35dd1b94beb6c2cac34f1d49c5824d03de5a1
    10.18.47.24 c0e481d8f55dbb7de078cdcf67ebf627dc371e969e7dbb0b93afcce104e9247e
    ```

* The flag is the SHA256 hash of the output file. Example:
    ```
    jctf{138706baa74bac72c8ee1c42eb3a7c6add2f71c0737c5044dcdd9cba7409ead6}
    ```

## Hint
* Verify that the end of your file has a new blank line.

## Solution
* Saya tinggal mengikuti instruksi yang ada pada challenge ini dan membuat script python seperti ini
```python
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

```
* mengecek hash pada file output menggunakan sha256sum
  
![](./Screenshot%202022-04-11%20124959.png)
  
* Flag: `jctf{90dc97926e09a45aa02ca3a95db387bb00ff83ccff18f4d18a3eb96b4893e8bb}`



## Credit
* Developed by Kevin McKenzie