'''Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.'''
n = int(input('Escribe un entero: '))
def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n-1)
print(factorial(n))