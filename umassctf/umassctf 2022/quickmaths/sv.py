from pwn import *

r = remote('34.148.103.218', 1228)

r.recvuntil(b'Good luck!')
r.recvline()
#r.recvline()

#p = eval(r.recvline().decode())
#r.sendline(str(p).encode())
#r.interactive()
for i in range(1000):
    r.recvline()
    x = eval(r.recvline().decode())
    r.sendline(str(x).encode())

r.interactive()
