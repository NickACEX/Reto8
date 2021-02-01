#Importamos Menu
from helpers.menu import Menu
from controllers.libros import LibrosController
from controllers.usuarios import UsuariosController

#Creamos el Menu de la APP
def app():
    try:
        print('''
        +++++++++++++++++++++++++++++++
              Sistema de Biblioteca
        +++++++++++++++++++++++++++++++
        ''')
        menu_principal=['Libros', 'Usuarios','Prestamo','Salir']
        respuesta=Menu(menu_principal).show()
        
        if respuesta==1:
            libro=LibrosController()
            libro.menu()
            if libro.salir:
                app()
        elif respuesta==2:
            usuario=UsuariosController()
            usuario.menu()
            if usuario.salir:
                app()
        elif respuesta==3:
            curso=CursoController()
            curso.menu()
            if curso.salir:
                app()

        print('\n Gracias por utilizar nuestro sistema \n')
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicacion')
    except Exception as e:
        print(f'{str(e)}')

app()