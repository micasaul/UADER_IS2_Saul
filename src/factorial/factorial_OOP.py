import sys

class Factorial:
    def __init__ (self):
        pass

    def run (self, min, max):
        if min < 0: 
            print("Factorial de un número negativo no existe")
            return 0
        else: 
            fact = 1
            while(max >= min): 
                fact *= max 
                max -= 1
            return fact 
        
if len(sys.argv) == 0 or not "-" in sys.argv[1]:
    print("Debe informar un rango!")
    sys.exit()

a, b = sys.argv[1].split("-")
if a == "":
    min = 1
else:
    min = int(a)
if b == "":
    max = 60
else:
    max = int(b)

factorial = Factorial()
print("Factorial ",min, "-", max,"! es ", factorial.run(min, max)) 