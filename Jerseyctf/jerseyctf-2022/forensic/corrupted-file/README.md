# corrupted file

## Challenge Text
* Can you find a way to fix our corrupted .jpg file?

## Hint
* no hint

## Solution

* diberi file jpg yang corrupt
* cek binary file menggunakan tool `bless`
  ![](./flagmod.png)
* tidak terlihat header file jpg
* tambahkan header file jpg yaitu `FF D8 FF`
  ![](./flagmod2.png)
* cek trailer file, ternyata sudah sesuai trailer jpg `FF D9`
  ![](./flagmod3.png)
* setelah mengubah header, file jpg dapat dilihat
* terlihat flag dalam gambar jpg

![](./flag_mod.jpg)

* Flag: `jctf{OaZdSdMo8F}`