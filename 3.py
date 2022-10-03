#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    
    u = set("abcdefghijklmnopqrstuvwxyz")
    
    A = {"c", "f", "h", "l", "o"}
    B = {"d", "e", "f", "p", "w"}
    C = {"j", "k"}
    D = {"b", "d", "g", "k", "t", "u", "y", "z"}
   
    X = (A.difference(B)).intersection(C.difference(D))

    nC = u.difference(C)
    nB = u.difference(B)
    
    Y = (A.difference(D)).union(nC.difference(nB))

    
    print(X)  
    print(Y)
