import os 

list_programacion=[]
list_rutas=[]
def fnt_limpiar ():
    os.system('cls')
    print('Nombre:Andres Felipe')
    print('Año:2024')
def fnt_agregar_ruta():
    fnt_limpiar()
    print('\n<<<< Consulatr')     
    
def fnt_consultar_rutas():
    fnt_limpiar()
    print('\n<<<<Consulatr rutas >>>\n')
    if len(list_rutas)== 0:
        print('\nNo hay rutas programadas')
    else:
        for i in range(len(list_rutas)):
            print(list_rutas[i])
    input('\nFin del regsitro <enter>')
def fnt_menu():
    fnt_limpiar()
    cod =input('Codigo:')
    nombre=('Nombre')
    descripcion=input('Descripcion')
    r = cod + ' ' + descripcion
    list_rutas.append(r)
    input('\nRuta registrada con exito <enter>')
def fnt_menu():
    fnt_limpiar()
    opcion_r= input('<< Menu de rutas >>\n1.Agregar\n2.Consultar\n3.Salir\n->')
    if opcion_r == '1':
        fnt_agregar_ruta()
    if opcion_r == '2 ':
        fnt_consultar_rutas()
    if opcion_r=='3':
        sw2= False
def fnt_envio():
    fnt_limpiar()
    print('<<< RUTAS DISPONIBLES >>>>')
    for i in range(len(list_rutas)):
        print(list_rutas)
    print('\n<<< Datos del envio >>>>')
    n_envio = input('Numero del envio')
    nombre = input('Nombre del cliente')
def fnt_consultar_envios():
    fnt_limpiar()
    print('')   
global sw 
sw = True
while sw == True:
    fnt_limpiar()
    opcionstr=input('<<< Menu principal >><\n1.Rutas\m2.Envios\n3.Salir\n->')
    if opcionstr == '1':
        fnt_menu()
    if opcionstr == '2':
        fnt
    