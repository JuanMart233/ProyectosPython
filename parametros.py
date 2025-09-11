def suma(a,b):
    resultado= a+b
    print(resultado)

def suma2(*args):
    s1 = 0
    for x in args:
        s1+=x
    return s1

print(suma(45,20))
print(suma2(45,20,2,2,2,2,2,2,2,2,2,2,2,2,2,2))