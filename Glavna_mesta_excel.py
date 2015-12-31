#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import random
y="d"
value=0
book = xlrd.open_workbook("Glavna_mesta_Evrope.xls")
sheet = book.sheet_by_name(sheet_name="Excel_template")
number_of_rows=sheet.nrows
while y=="d" or y!="n":
   if y=="d":
      value=random.choice(range(number_of_rows))
      ws=sheet.row_values(value)[0]
      print "V angleskem jeziku ugani glavno mesto evropske drzave", ws
      ugani_gm=raw_input()
      gm=sheet.row_values(value)[1]
      if ugani_gm==gm:
         print "Bravo, uganil si glavno mesto, zelis nadaljevati (d/n)?"
         y=raw_input()
      else:
         print "Ni ti uspelo, zelis nadaljevati igro (d/n)?"
         y=raw_input()
   elif y!="d" or y!="n":
      print "Nisi pravilno dogovoril na vprasanje. Vnesi d oz. n:"
      y=raw_input()