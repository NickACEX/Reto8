#importamos metodos de  Modelo Libros
from models.libros import Libros
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question

#Nuestros metodos
class LibrosController:
    def __init__(self):
        self.libros=Libros()
        self.salir=False
    
    def menu(self):
        try:
            while True:
                print('''
                =============================
                            Libros
                =============================
                ''')
                lista_menu=['Listar','Buscar','Crear','Salir']
                respuesta=Menu(lista_menu).show()

                if respuesta==1:
                    self.all_libro()
                elif respuesta==2:
                    self.search_libro()
                elif respuesta==3:
                    self.insert_libro()
                else:
                    self.salir=True
                    break  

        except Exception as e:
            print(f'{str(e)}')

    def all_libro(self):
        print('''
        =============================
              Listar Libros
        =============================
        ''')
        libro=self.libros.get_libros('libro_id')
        print(print_table(libro,['Libro_Id','Nombre','Autor','Editorial','Estatus']))
        input('\nPresiona una tecla para continuar . . .')

    def search_libro(self):
        self.all_libro()
        print('''
        =============================
               Buscar Usuario
        =============================
        ''')
        try:
            libro_id=input_data('Ingrese el ID del Libro : ','int')
            libro=self.libros.get_libro({
                'libro_id': libro_id
            })
            print(print_table(libro,['Libro_Id','Nombre','Autor','Editorial','Estatus']))
            if libro:
                if question('Desea dar mantenimiento al Libro?'):
                    opciones=['Editar Libro','Eliminar Libro','Salir']
                    respuesta=Menu(opciones).show()
                    if respuesta==1:
                        self.update_libro(libro_id)
                    elif respuesta==2:
                        pass
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar . . .')

    def update_libro(self, libro_id):
        nombre=input_data('Ingrese el Nombre del Libro : ')
        autor=input_data('Ingrese el Autor del Libro : ')
        editorial=input_data('Ingrese la Editorial Libro : ')
        estatus='ACTIVO'
        self.libros.update_libro({
            'libro_id':libro_id
        },{
            'nombre':nombre,
            'autor':autor,
            'editorial':editorial,
            'estatus':estatus
        })
        print('\n Datos del Libro Actualizado \n')

    def insert_libro(self):
        nombre=input_data('Ingrese el Nombre del Libro : ')
        autor=input_data('Ingrese el Autor del Libro : ')
        editorial=input_data('Ingrese la Editorial Libro : ')
        estatus='ACTIVO'
        self.libros.insert_libro({
            'nombre':nombre,
            'autor':autor,
            'editorial':editorial,
            'estatus':estatus
        })
        print('''
        =============================
           Listar Libro Agregado
        =============================
        ''')    
        self.all_libro()

