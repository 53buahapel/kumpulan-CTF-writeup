from multiprocessing.pool import Pool
from sys import argv
import requests

# I used /opt/dirbuster/directory-list-2.3-small.txt for the file,
# other parameters are self-explanatory
if len(argv) != 4:
    print(f'Usage: {argv[0]} <URL> <brute force file> <num threads>')
    exit(1)

url = argv[1]
fname = argv[2]
numthreads = int(argv[3])

# Prints out the flag if it's in the content of this page
def check_page(name):
    name = name.strip()
    r = requests.get(f'{url}/{name}')
    if 'jctf' in r.text:
        print(r.text)

# Uses a process pool to check all of the pages with names from the file
with open(fname, 'r') as f:
    with Pool(processes=numthreads) as pool:
        pool.map(check_page, f, 256)