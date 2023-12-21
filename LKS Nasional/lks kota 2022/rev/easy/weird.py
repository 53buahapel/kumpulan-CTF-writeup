password = [
    70,
    65,
    89,
    89,
    71,
    65,
    113,
    62,
    60,
    50,
    107,
    51,
    61,
    104,
    61,
    110,
    59,
    63,
    59,
    60,
    61,
    61,
    59,
    107,
    63,
    58,
    110,
    50,
    57,
    56,
    59,
    62,
    104,
    50,
    61,
    61,
    110,
    50,
    108,
    119,
]


p = input("> ")
counter = 0
for i in p:
    t = ord(i) ^ 10
    if t == password[counter]:
        counter += 1
        continue
    else:
        print("Salah")
    counter += 1

a = []
for i in password:
    a.append(chr(i ^ 10 ))
print("".join(a)) # LKSSMK{468a97b7d1516771a50d83214b877d8f}
