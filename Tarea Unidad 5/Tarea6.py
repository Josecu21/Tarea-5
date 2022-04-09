'''Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.'''
import math
a=int(input('Ingrese el radio: '))
def calcArea(a):
    area=math.pi*(a**2)
    perimetro=2*math.pi*a
    print('{:.2f}'.format(area))
    print('{:.2f}'.format(perimetro))
calcArea(a)
    