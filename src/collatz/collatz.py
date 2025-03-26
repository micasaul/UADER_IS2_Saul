import matplotlib.pyplot as plt

def collatz(n):
    it = 0
    while n!=1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        it += 1
    return it

num = range(1, 1001)
iteraciones= []

for i in num:
    iteraciones.append(collatz(i))

plt.figure(figsize=(10, 5))
plt.scatter(num, iteraciones, s=2)
plt.title("Conjetura de Collatz")
plt.xlabel("Números")
plt.ylabel("Iteraciones")
plt.grid(True)
plt.show()