#!/usr/bin/python

import operator
import random
import sys
from datetime import datetime


def print_(data):
    sys.stdout.write(data + "\n")
    sys.stdout.flush()


def clientThread():
    print_(
        "Selamat Datang di LKS SMK\n Untuk 1 Soal memiliki 1 Poin.\nDapatkan 10 poin untuk membuka flag. Waktu 5 detik.\n\n"
    )

    start_time = datetime.now()
    score = 0
    for i in range(10):
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }
        num1 = random.randint(1000, 9999)
        num2 = random.randint(1000, 9999)
        op = random.choice(list(ops.keys()))
        answer = float(ops.get(op)(num1, num2))
        print_("No: (" + str(i + 1) + ") {} {} {} =>  ".format(num1, op, num2))
        data = input()

        now_time = datetime.now()
        delta_time = now_time - start_time
        if delta_time.total_seconds() > 5:
            print_("\n\nwaktu habis\n\n")
            return None

        try:
            data = float(data)
            if data == answer:
                score = score + 1
                print_("~~> {} ({})\n\n".format(data, str("correct")))
            else:
                print_("~~> {} ({})\n\n".format(data, str("wrong")))
        except:
            print_("~~> {} ({})\n\n".format(data, str("wrong")))

    print_("Score: " + str(score) + "\n")

    if score == 10:
        print_("\n\nanda lulus, tapi tidak ada flag disini")
    else:
        print_("\n\ncoba lagi\n\n")

    return


def main():
    clientThread()


main()
