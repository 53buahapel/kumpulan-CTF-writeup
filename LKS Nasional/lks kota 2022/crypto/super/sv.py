from base64 import b64decode

f = open('super64.txt', 'r').read()

c = 0

while True:
  f = b64decode(f)
  c += 1
  if b'LKS' in f:
    print(f)
    print('Found in {} iterations'.format(c))
    break

  # LKSSMK{Supeeerrrrrr_Base64_Encoding}