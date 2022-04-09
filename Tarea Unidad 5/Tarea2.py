'''Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.'''

def EsMultiplo():
    a = int(input('Ingrese un número: '))
    b = int(input('Ingrese otro número: '))
    if a % b==0:
        print(f'El número {a} es multiplo de {b}')
    
    elif b % a==0:
        print(f'El número {b} es multiplo de {a}')
    else:
        print('Los números ingresados no son multiplos')
EsMultiplo()
