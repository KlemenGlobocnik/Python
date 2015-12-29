import random
y="d"
d={"Albania":"Tirane",
"Andorra":"Andorra-la-vella",
"Armenia":"Jerevan",
"Austria":"Vienna",
"Azerbaijan":"Baku",
"Belarus":"Minsk",
"Belgium":"Brussels",
"Bosnia & Herzegovina":"Sarajevo",
"Bulgaria":"Sofia",
"Croatia":"Zagreb",
"Cyprus":"Nicosia",
"Czech Republic":"Prague",
"Denmark":"Copenhagen",
"Estonia":"Tallinn",
"Finland":"Helsinki",
"France":"Paris",
"French Guiana":"Cayenne",
"Georgia":"Tbilisi",
"Germany":"Berlin",
"Greece":"Athens",
"Hungary":"Budapest",
"Iceland":"Reykjavik",
"Italy":"Rome",
"Latvia":"Riga",
"Liechtenstein":"Vaduz",
"Lithuania":"Vilnius",
"Luxemburg":"Luxemburg",
"Macedonia":"Skopje",
"Malta":"Valletta",
"Martinique":"Fort-de-France",
"Moldova":"Kishinev",
"Monaco":"Monaco",
"Netherlands":"Amsterdam, The Hague (political Capital)",
"Norway":"Oslo",
"Northern Ireland":"Belfast",
"Poland":"Warsaw",
"Portugal":"Lisbon",
"Romania":"Bucharest",
"Russia":"Moscow",
"San Marino":"San Marino",
"Scotland":"Edinburgh",
"Slovakia":"Bratislava",
"Slovenia":"Ljubljana",
"Spain":"Madrid",
"Sweden":"Stockholm",
"Switzerland":"Berne",
"Tajikistan":"Dushanbe",
"Ukraine":"Kiev",
"United Kingdom":"London",
"Uzbekistan":"Toshkent/Tashkent",
"Vatican City":"Vatican City",
"Yugoslavia":"Belgrade"}
while y=="d" or y!="n":
    if y=="d":
        ws=random.choice(d.keys())
        print "V angleskem jeziku ugani glavno mesto evropske drzave", ws
        ugani_gm=raw_input()
        if ws in d.keys():
            gm = d[ws]
            if ugani_gm==gm:
                print "Bravo, uganil si glavno mesto, zelis nadaljevati (d/n)?"
                y=raw_input()
            else:
                print "Ni ti uspelo, zelis nadaljevati igro (d/n)?"
                y=raw_input()
    elif y!="d" or y!="n":
        print "Nisi pravilno dogovoril na vprasanje. Vnesi d oz. n:"
        y=raw_input()




