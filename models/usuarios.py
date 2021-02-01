from connection.conn import Connection

class Usuarios:
    def __init__(self):
        self.model = Connection('usuarios')

    def get_usuarios(self, order):
        return self.model.get_all(order)

    def get_usuario(self, id_object):
        return self.model.get_by_id(id_object)

    def search_usuario(self, data):
        return self.model.get_columns(data)

    def insert_usuario(self, usuario):
        return self.model.insert(usuario)

    def update_usuario(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_usuario(self, id_object):
        return self.model.delete(id_object)
