X=50
mipapa=(input("Adivina el valor de X, teclea un numero y ve acercandote al valor "))
if mipapa <= X:
    print("tu numero es inferior a X")
else:
    if mipapa >= X:
        print("tu numero es mayor a X")
    else:
        if mipapa == 0:
            print("tu numero es igual a X")