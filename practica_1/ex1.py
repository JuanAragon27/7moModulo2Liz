#First ex "Hello World"
print("Hello World")

n = int(input("Dame un número: "))
lista = []
contador = 0
for i in range(1, n + 1):
    if n % i == 0:
        for j in range (n + 1, n % i == 0 ):
            contador = contador + 1
            lista.append(j)
            print(lista)

