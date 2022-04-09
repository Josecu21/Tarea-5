'''Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.'''
def calculartiempo():
    print('1) Calcular de segundos a Horas con minutos y segundos')
    print('2) Calcular de horas minutos y segundos a segundos')
    print('3) Salir del programa')
    b=int(input('Escoja la opcion que desee ejecutar: '))
    if b==1:
        def horSegundos():
            d=int(input('Ingrese las segundos: '))
            hora1= int(d/60/60)
            minu= int(d/60%60)
            segundos= int(d%60)
            print(hora1,'Horas con',minu,'minutos y',segundos,'segundos')
        horSegundos()
    elif b==2:
        def segunHoras():
            a=int(input('Ingrese las horas: '))
            b=int(input('Ingrese las minutos: '))
            c=int(input('Ingrese las segundos: '))
            segundos1= a*60*60
            segundos2= b*60
            segundostotales= segundos1+segundos2+c
            print(segundostotales,' segundos')
        segunHoras()
    elif b==3:
        print('Salio con exito')
calculartiempo()
