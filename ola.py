numeros = {4,8,2,7,1,9,3,5}
total = 0
#solo sumar los numeros impares
for num in numeros:
    if num % 2 == 0:
        print("numero par, no solo sumamos")
        continue
    total += num