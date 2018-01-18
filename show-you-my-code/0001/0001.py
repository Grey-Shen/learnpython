#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string


def create_coupons(amount, length):
    f = open('coupons.txt', 'w')
    for i in range(amount):
        base = string.ascii_letters + string.digits
        print("base = {}".format(base))
        c = [random.choice(base) for i in range(length)]
        print("c = {}".format(c))
        f.write(''.join(c) + '\n')
    f.close()

if __name__ == "__main__":
    amount = 200
    length = 12
    create_coupons(amount, length)
