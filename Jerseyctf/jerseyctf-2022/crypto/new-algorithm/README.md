# new-algorithm

## Challenge Text
* On the first day of the job, a new cryptography intern is insisting to upper management that he developed a new encryption algorithm for the company to use for sensitive emails and should get a raise. This seems too good to be true... are you able to prove the intern wrong by decrypting it?
* Here's an example of an encrypted email message using the intern's algorithm: `amN0Znt0UllfQUVTX0lOc1QzQGR9`

## Hint
* What are some differences between encryption, encoding, and hashing?

## Solution
* setelah melihat Hint diketahui bahwa cypher text tersebut adalah enkripsi base 64, lalu saya mendecode tersebut menggunakan [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=YW1OMFpudDBVbGxmUVVWVFgwbE9jMVF6UUdSOQ)

* Flag: `jctf{tRY_AES_INsT3@d}`
