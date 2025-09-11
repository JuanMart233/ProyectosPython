x = input("teclea el valor del numero que deseas calcular al factorial ")
factorial = 1
for z in range(1,int(x)+1):
    factorial*= z
print("el factorial de " + str(x)+" es "+str(factorial))