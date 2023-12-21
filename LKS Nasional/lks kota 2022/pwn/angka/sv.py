from pwn import *

r = remote('116.193.191.147',20000)
for i in range(1,11):
    r.recvuntil(f'No: ({i})'.encode())

    p = eval(r.recv(12).strip())
    r.sendlineafter(b'=> ', str(p).encode())
    print(p)

r.interactive()

# LKSSMK{Soal_Matematika_EZ_Sekali}