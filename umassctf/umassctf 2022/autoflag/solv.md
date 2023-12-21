## Unsecure JWT

Provided sorce code from the web itself.

https://github.com/UMassCybersecurity/AutoFlag-API

```js
function base64url(source) {
    encodedSource = btoa(source);
    while (encodedSource.endsWith('=')) {
        encodedSource = encodedSource.substring(0, encodedSource.length - 1)
    }
    encodedSource = encodeURI(encodedSource)
    console.log(encodedSource)
    return encodedSource;
}

function getSignedHMAC(unsignedToken) {
    return new Promise((resolve, reject) => {
        var xhr = new XMLHttpRequest()
        xhr.open("POST", '/api/sign-hmac', true)

        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")

        xhr.onreadystatechange = function () { // Call a function when the state changes.
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                resolve(xhr.responseText)
            }
        }
        xhr.send(`message=${unsignedToken}`)
    })
}

async function signToken() {
    header = `{"typ":"JWT","alg":"HS256"}`
    data = `{"fresh":false,"iat":1648755893,"jti":"a5139f01-3e20-446c-9627-16580f32f118","type":"access","sub":"anonymous","nbf":1648755893,"exp":1648756793}`
    unsignedToken = base64url(header) + "." + base64url(data)
    console.log(unsignedToken)
    let signature = await getSignedHMAC(unsignedToken)
    signature = signature.replaceAll('+', '-').replaceAll('=', '')
    let JWT = unsignedToken + "." + signature
    return JWT
}

signToken()

document.getElementById('redir').innerText = 'Redirecting you to your flag shortly'
setTimeout(() => {
    window.location.replace("/flag");
}, 2000)
```
- To analyze check the first commit. The author delete an entire code at recent commit
  
We can see there's flow code from signToken() function

- Change the username anonymous to admin
- generate using Hmac using getHmac 
- generate JWT using signToken() 
- paste to cookie 
- get the flag

### flag
UMASS{W0W_TH1$_1$_4_C00L_FL4G_BRUH!_69420}