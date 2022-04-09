'''Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.'''
import numpy as np
lista=[]
a=int(input('Cuantos números desea ingresar?: '))
def CalcularMaxMin(lista):
    for i in range(a):
        b=int(input('Ingrese un número '))
        lista.append(b)
        lista.sort()
    print(lista)
    print(range(a))
    print('el mayor número es',np.amax(lista))
    print('el menor número es',np.amin(lista))
CalcularMaxMin(lista)

