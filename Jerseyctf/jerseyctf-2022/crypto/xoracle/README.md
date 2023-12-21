# xoracle

## Challenge Text
* Check out my cool new encryption service! It's very secure! Connect to 0.cloud.chals.io on port 19305.

## Hint
* Read carefully: a small mistake or typo can be all it takes to make an encryption system insecure.

## Solution

* Saya menggunakan netcat untuk connect ke server.
  ```sh
  nc 0.cloud.chals.io 19305
  ```
* memasukan lagi byte string ke server

![](./Screenshot%202022-04-11%20104523.png)

* mendecode hex `6a6374667b315f746830553968545f31745f7734355f3533437572655f61303762386130317d` menggunakan [cyberchef <---](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NmE2Mzc0NjY3YjMxNWY3NDY4MzA1NTM5Njg1NDVmMzE3NDVmNzczNDM1NWYzNTMzNDM3NTcyNjU1ZjYxMzAzNzYyMzg2MTMwMzE3ZA)
* Flag: `jctf{1_th0U9hT_1t_w45_53Cure_a07b8a01}`

## Credit
* Developed by [ContronThePanda](https://github.com/PAndaContron), part of [RUSEC](https://rusec.github.io/).