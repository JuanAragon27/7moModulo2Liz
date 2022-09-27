#Exercise of arrays from 1 to n , you must observe the links between primos
import sys

m=sys.argv
z=int(m[1])
global my_array
my_array=[]
global my_new_array
my_new_array=[]

def my_number(z):
    for i in range (1,z+1):
        my_array.append(i)
        
def primos(z):
    global flag
    flag=0
    for i in range (1,z):
        x=int(my_array[i])
        flag=0
        for c in range (1,x):
            if (x/c)!=0 :
               flag=flag+1
            if flag <=2:
                my_new_array.append(i)
                print(my_new_array)
            
            
            

print(my_new_array)
my_number(z)
primos(z)