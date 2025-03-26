#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(desde, hasta): 
    if desde < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    else: 
        fact = 1
        while(hasta >= desde): 
            fact *= hasta 
            hasta -= 1
        return fact 

if len(sys.argv) == 0:
   print("Debe informar un número!")
   sys.exit()

if "-" in sys.argv[1]:
    desde, hasta = sys.argv[1].split("-")
    desde = int(desde)
    hasta = int(hasta)
else:
    desde = 1
    hasta = int(sys.argv[1])

print("Factorial ",desde, "-", hasta,"! es ", factorial(desde, hasta)) 