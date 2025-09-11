# sirve para simplificar, mantenimiento mas pesado, su vengaja es que abstraigo lo que quiero y lo uso en otro lado
# para llamar a una funcion solo hay que escribir el nombre de la funcion seguida de los parametros ( si los hubiera )entre parentesis
def saludo(nombre):
    print("hola, "+ nombre +". !bienvenido!")
saludo("angel")
def saludo2(nombre="anonimo"):
    print("hola, "+ nombre +". !bienvenido!")
saludo()