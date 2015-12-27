Nakupovalni_listek=[]
vprasanje="d"
while vprasanje!="n" or vprasanje=="d":
    vprasanje=raw_input("Zelis nakupovati (d/n)>>")
    if vprasanje == "d":
        nov_izdelek=raw_input("Vnesi izdelek, ki ga zelis kupit!>>")
        Nakupovalni_listek.append(nov_izdelek)
    elif vprasanje!="n" or vprasanje!="d":
        print "Napaka pri vnosu, vnesi d ali n!"
    else:
        break
print Nakupovalni_listek
for x in Nakupovalni_listek:
    print x
