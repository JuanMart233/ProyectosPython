global a
def calcula():
    a = 1
    print("dentro de la funcion: ", a)
    a = 5
    calcula()
    print("fuera de la funcion: ", a)
