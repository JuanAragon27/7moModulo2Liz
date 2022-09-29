#Exercise of arrays from 1 to n , you must observe the links between primos
import sys

m=sys.argv
z=int(m[1])
global my_array
my_array=[]
global my_new_array
my_new_array=[1]

def my_number(z):
    for i in range (1,z+1):
        my_array.append(i)
        
def Primos(z):
    cont = 0
    for i in range(2, z + 1):
        primos = True
        for j in range(2,i):
            if i == j:
               break
            elif i%j == 0:
               primos = False
            else:
               continue
        if primos == True:
            my_new_array.append(i)
            cont += 1
            print(my_new_array)
my_number(z)
Primos(z)