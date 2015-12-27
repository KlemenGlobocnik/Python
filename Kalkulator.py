# -*- coding: utf-8 -*-
c="y"
x=0
y=0
while c!="n" and True:
    try:
        x=raw_input("vnesi prvo stevilo: ")
        y=raw_input("vnesi drugo stevilo: ")
        z=raw_input("vnesi operator +,-,*,/")
        if z=="+":
            print float(x)+float(y)
        elif z=="-":
            print float(x)-float(y)
        elif z=="*":
            print float(x)*float(y)
        elif z=="/":
            print float(x)/float(y)

        c=raw_input("Zelis se racunati, vnesi y za da oz. n za ne: ")
    except ValueError:
        c=raw_input("Napacen vnost stevila. Zelis ponoviti izracun, za da vnesi y, za ne vnesi n: ")

