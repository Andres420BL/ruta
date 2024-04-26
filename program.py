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


