## Judul Soal
weird qr

## Deskripsi Soal
my qr web generator is so weird

---
## Proof of Concept
- local file inclusion

## solve

1. membaca script yang ada di dalam folder
2. terdapat filter untuk protocol `file:// gopher:// ftp://`
3. flag terdapat di dalam web.py
4. menggunakan protocol `local_file://` untuk membaca file yang ada di dalam folder
5. [generate](https://www.qr-code-generator.com/) qr code dengan payload seperti ini `local_file:///proc/self/environ/web.py` 
![](frame.png)
## Flag

under construction :D