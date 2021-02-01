from connection.conn import Connection

class Prestamo:
    def __init__(self):
        self.model = Connection('prestamos')

    def get_prestamos(self, order):
        return self.model.get_all(order)

    def get_prestamo(self, id_object):
        return self.model.get_by_id(id_object)

    def search_prestamo(self, data):
        return self.model.get_columns(data)

    def insert_prestamo(self, prestamo):
        return self.model.insert(prestamo)

    def update_prestamo(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_prestamo(self, id_object):
        return self.model.delete(id_object)
