import os 

list_programacion=[]
list_rutas=[]
def fnt_limpiar ():
    os.system('cls')
    print('Nombre:')
    print('Autor')
    
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
    if opcion_r=='3':
        sw2= False

