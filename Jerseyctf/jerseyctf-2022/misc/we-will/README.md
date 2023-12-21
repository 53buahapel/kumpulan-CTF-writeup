# we-will

## Challenge Text
* A flag was left behind but it seems to be protected.

## Hint
* The challenge name should help you figure out how to open it.

## Solution
* Nama challenge nya we will, terus saya keinget lagu Queen we will `rockyou!`
* Lalu saya melakukan bruteforce menggunakan wordlist rockyou dengan membuat script python seperti ini
```python
import zipfile


def crack_password(password_list, obj):
	# tracking line no. at which password is found
	idx = 0

	# open file in read byte mode only as "rockyou.txt"
	# file contains some special characters and hence
	# UnicodeDecodeError will be generated
	with open(password_list, 'rb') as file:
		for line in file:
			for word in line.split():
				try:
					idx += 1
					obj.extractall(pwd=word)
					print("Password found at line", idx)
					print("Password is", word.decode())
					return True
				except:
					continue
	return False


password_list = "rockyou.txt"

zip_file = "flag.zip"

# ZipFile object initialised
obj = zipfile.ZipFile(zip_file)

# count of number of words present in file
cnt = len(list(open(password_list, "rb")))

print("There are total", cnt,
	"number of passwords to test")

if crack_password(password_list, obj) == False:
	print("Password not found in this file")
```
* setelah menjalankan script saya mendapatkan password dan dapat melihat file flag.txt yang terdapat di dalam zip
 
![](./Screenshot%202022-04-11%20151346.png)

* Flag : `jctf{y0u_r0ck3d_17}`

## Credit
* Developed by [Rob](https://github.com/njccicrob)