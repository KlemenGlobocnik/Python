ime_datoteke="text2.txt"
datoteka=open(ime_datoteke,"r")

with open(ime_datoteke, "r") as datoteka:
    text = datoteka.read()
    bl_crna=text.count("CCAGCAATCGC")
    bl_rjava=text.count("GCCAGTGCCG")
    bl_korencek=text.count("TTAGCTATCGC")
    oo_kvadraten=text.count("GCCACGG")
    oo_okrogel=text.count("ACCACAA")
    oo_ovalen=text.count("AGGCCTCA")
    bo_modra=text.count("TTGTGGTGGC")
    bo_zelena=text.count("GGGAGGTGGC")
    bo_rjava=text.count("AAGTAGTGAC")
    s_moski=text.count("TGCAGGAACTTC")
    s_zenska=text.count("TGAAGGACCTTC")
    r_belec=text.count("AAAACCTCA")
    r_crnec=text.count("CGACTACAG")
    r_azijec=text.count("CGCGGGCCG")

if s_moski>0 and r_belec>0 and bl_korencek>0 and bo_rjava>0 and oo_okrogel>0:
    print ("Ziga je osumljenec")
else:
    print ("Ziga ni osumljenec")

if s_moski>0 and r_belec>0 and bl_crna>0 and bo_modra>0 and oo_ovalen>0:
    print ("Matej je osumljenec")
else:
    print ("Matej ni osumljenec")

if s_moski>0 and r_belec>0 and bl_rjava>0 and bo_zelena>0 and oo_kvadraten>0:
    print ("Miha je osumljenec")
else:
    print ("Miha ni osumljenec")












