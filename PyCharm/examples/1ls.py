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
    s = sum(a for a in A if abs(a) < 5)
    print(s)
