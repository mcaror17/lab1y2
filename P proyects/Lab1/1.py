class Lista:
    def __init__(obj, lista):
        obj.lista = lista

    def max (obj):
        maximo = obj.lista[0]
        for i in range (1,len(obj.lista)):
            if (obj.lista[i] >= maximo):
                maximo = obj.lista[i]
        return maximo

    def min (obj):
        minimo = obj.lista[0]
        for i in range (1,len(obj.lista)):
            if (obj.lista[i] <= minimo):
                minimo = obj.lista[i]
        return minimo

    def suma (obj):
        s = 0
        for i in range (0,len(obj.lista)):
            s += obj.lista[i]
        return s

    def promedio (obj):
        s = obj.suma()
        promedio = s/len(obj.lista)
        return promedio

n = int(input("¿Cuantos números va a ingresar?: "))
L = []
for i in range (0,n):
    L += [int(input(f"Ingrese el número {i+1}: "))]

l1 = Lista(L)
print(l1.max())
print(l1.min())
print(l1.suma())
print(l1.promedio())

