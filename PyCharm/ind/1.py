#!/usr/bin/env pethon3
# -*- coding: utf -8 -*-

import sys

if __name__ == '__main__':
    # ввести кортеж одной строчкой
    a = tuple(map(int, input("enter tuple ").split()))
    b = ()

    b_l = list(b)

    # проверка на количество элементов
    for i, item in enumerate(a):
        if (i+1) % 2 == 0:
            b_l.append(item ** 2)
        else:
            b_l.append(item * 2)

    b = tuple(b_l)
    print (f'a={a}\nb={b}')


