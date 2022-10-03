#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":

    u = {"a", "e", "i", "o", "u", "y"}
    print("Введите строку")
    stroka = str(input())
    k = 0
    for i in stroka:
        dd1 = i
        dd2 = set(dd1)
        f = u.intersection(dd2)
        dlinna = len(f)
        k = k + dlinna

    print(k)
