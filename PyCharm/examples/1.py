#!/usr/bin/nev python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    # проверить количество элементов кортежа.
    if len(A) != 10:
        print("неверный размер кортежа", file=sys.stderr)
        exit(1)

    # найти искомую сумму.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item

    print(s)
