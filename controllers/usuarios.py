#importamos metodos de  Modelo Libros
from models.usuarios import Usuarios
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question

#Nuestros metodos
class UsuariosController:
    def __init__(self):
        self.usuarios=Usuarios()
        self.salir=False
    
    def menu(self):
        try:
            while True:
                print('''
                =============================
                            Usuarios
                =============================
                ''')
                lista_menu=['Listar','Buscar','Crear','Salir']
                respuesta=Menu(lista_menu).show()

                if respuesta==1:
                    self.all_usuario()
                elif respuesta==2:
                    self.search_usuario()
                elif respuesta==3:
                    self.insert_usuario()
                else:
                    self.salir=True
                    break  

        except Exception as e:
            print(f'{str(e)}')

    def all_usuario(self):
        print('''
        =============================
              Listar Usuarios
        =============================
        ''')
        usuario=self.usuarios.get_usuarios('usuario_id')
        print(print_table(usuario,['Usuario_Id', 'Nombre', 'Apellido', 'Correo', 'Celular']))
        input('\nPresiona una tecla para continuar . . .')

    def search_usuario(self):
        self.all_usuario()
        print('''
        =============================
               Buscar Usuario
        =============================
        ''')
        try:
            usuario_id=input_data('Ingrese el ID del Usuario : ','int')
            usuario=self.usuarios.get_usuario({
                'usuario_id': usuario_id
            })
            print(print_table(usuario,['Usuario_Id', 'Nombre', 'Apellido', 'Correo', 'Celular']))
            if usuario:
                if question('Desea dar mantenimiento al Usuario?'):
                    opciones=['Editar Usuario','Eliminar Usuario','Salir']
                    respuesta=Menu(opciones).show()
                    if respuesta==1:
                        self.update_usuario(usuario_id)
                    elif respuesta==2:
                        pass
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar . . .')

    def update_usuario(self, usuario_id):
        nombre=input_data('Actulice el Nombre del usuario : ')
        apellido=input_data('Actulice los Apellidos del usuario : ')
        correo=input_data('Actulice el Correo del usuario : ')
        celular=input_data('Actulice el Celular del usuario : ')
        self.usuarios.update_usuario({
            'usuario_id':usuario_id
        },{
            'nombre':nombre,
            'apellido':apellido,
            'correo':correo,
            'celular':celular
        })
        print('\n Datos del Usuario Actualizado \n')

    def insert_usuario(self):
        nombre=input_data('Ingrese el Nombre del usuario : ')
        apellido=input_data('Ingrese los Apellidos del usuario : ')
        correo=input_data('Ingrese el Correo del usuario : ')
        celular=input_data('Ingrese el Celular del usuario : ')
        self.usuarios.insert_usuario({
            'nombre':nombre,
            'apellido':apellido,
            'correo':correo,
            'celular':int(celular)
        })
        print('''
        =============================
           Listar Libro Agregado
        =============================
        ''')    
        self.all_usuario()

