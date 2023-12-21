from pwn import *
from Crypto.Util.number import *
from gmpy2 import *

r = remote('challenge.nahamcon.com',32104)

def ricif():
    r.recvuntil(b'n = ')
    n = int(r.recvline().decode().strip())
    r.recvuntil(b'e = ')
    e = int(r.recvline().decode().strip())
    r.recvuntil(b'ct = ')
    ct = int(r.recvline().decode().strip())
    return n, e, ct

def part1():
    r.sendline(b'1')
    n,e,ct = ricif()
    p = fermat(n)[0]
    q = fermat(n)[1]
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    m = pow(ct, d, n).digits()
    r.sendline(str(m).encode())

def part2():
    n,e,ct = ricif()
    m = iroot(ct, 3)[0].digits()
    r.sendline(str(m).encode())

def part3():
    r.recvuntil(b'n = ')
    n,e,ct = ricif()
    p = fermat(n)[0]
    q = fermat(n)[1]
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    m = pow(ct, d, n).digits()
    r.sendline(str(m).encode())

def fermat(n):
    a = isqrt(n + 1)
    b = a * a - n
    while not is_square(b):
        b += 2 * a + 1
        a += 1
    p = a - isqrt(b)
    q = a + isqrt(b)
    return [p,q]

part1()
part2()
part3()
r.interactive()