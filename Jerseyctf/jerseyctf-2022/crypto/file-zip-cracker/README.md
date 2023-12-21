# file-zip-cracker

## Challenge Text
* We have a secret file that is password protected. However, we have obtained a wordlist of actors that is part of the password. The password is the combination of one of the names on the list with a year.
  * Format: "Actor_NameYYYY"  
  * Example: "Henry_Cavill1964"
* Fix the script to brute force the password.

## Hint
* No hints.

## Solution
* Terdapat kode yang salah dalam kracker lalu saya membenarkanya menjadi seperti ini
```python
import zipfile
import itertools
from itertools import permutations


# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        pass

# Main code starts here...
# The file name of the zip file.
zipfilename = 'secret_folder.zip'

Actor_Name = open('actorList.txt','r').readlines()

numbers_set = '0123456789'

zip_file = zipfile.ZipFile(zipfilename)

for i in Actor_Name:
    a = i.strip('\n')
    for c in itertools.product(numbers_set, repeat=4):
        password = a+''.join(c)
        print("Trying: %s" % password)
        if extractFile(zip_file, password):
            print('*' * 20)
            print('Password found: %s' % password)
            print('Files extracted...')
            exit(0)

# If no password was found by the end, let us know!
print('Password not found.')

```
* setelah menjalankan script sang saya benarkan(koreksi), akhirnya program bisa berjalan dengan baik.
* Di dalam folder tersebut terdapat pesan `Gur pbqr gb haybpx gur mvc svyr vf: v'ir_tbg_n_wne_bs_qveg_naq_thrff_jung'f_vafvqr_vg `
* Setelah saya decrypt pesan itu ternyata adalah `The code to unlock the zip file is: i've_got_a_jar_of_dirt_and_guess_what's_inside_it `
* Lalu saya ekstrak file zip yang ada lagi di dalam menggunakan kode tersebut
* Di dalam file tersebut terdapat file `Flag.mp3` namun file tersebut tidak bisa dibuka
* setelah saya cek file headernya ternyata itu merupakan file gif, lalu saya menggati format file tersebut menjadi `.gif`
* Flag: 
![flag](./secret_folder/compressed_file/Flag.gif)

## Credit
* Developed by [Nishaant Goswamy](https://www.github.com/nishaant215)