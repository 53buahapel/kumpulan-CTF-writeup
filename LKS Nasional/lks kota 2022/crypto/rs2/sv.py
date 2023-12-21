from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA
import gmpy2

key = open('public.key', 'rb').read()
rsa = RSA.importKey(key)
e = rsa.e
n = rsa.n

c = bytes_to_long(open('flag.enc', 'rb').read())

def FermatFactor(N):
    a = gmpy2.isqrt(N + 1)
    b = a*a - N
    while not gmpy2.is_square(b):
        b += 2*a + 1
        a += 1
    p = a - gmpy2.isqrt(b)
    q = a + gmpy2.isqrt(b)
    return [p, q]

p, q = FermatFactor(n)
tot = (p-1)*(q-1)
d = gmpy2.invert(e, tot)
m = pow(c, d, n)
print(long_to_bytes(m)) 
