X=50
Y=(input("Adivina el valor de X, teclea un numero y ve acercandote al valor "))
if Y <= X:
    print("tu numero es inferior a X")
else:
    if Y >= X:
        print("tu numero es mayor a X")
    else:
        if Y == 0:
            print("tu numero es igual a X")