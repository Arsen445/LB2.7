#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":

    u = {"a", "e", "i", "o", "u", "y"}
    print("Введите 2 строки")
    stroka1 = str(input())
    stroka2 = str(input())

    mnozestvo1 = set(stroka1)
    mnozestvo2 = set(stroka2)

    rezult = mnozestvo1.intersection(mnozestvo2)
    
    print(rezult)  
       
       


