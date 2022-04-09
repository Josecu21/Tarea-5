'''Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.'''

def usuario1():
    print('Registrate')
    global a
    a= str(input('Ingrese un usuario: '))
    global b
    b= input('Ingrese una contraseña: ')
    print('Registrado, ahora ingrese sus datos de nuevo')
usuario1()
    
def login():
    print('Loggeate')
    c= str(input('Ingrese su usuario: '))
    d= str(input('Ingrese su clave: '))
    while a==c and b==d:
        print('Logueado correctamente')
        if a!=c and b!=d:
            print('Error al momento de loguearte')
            return login() 
        elif login() in 3:
            break     
login()
