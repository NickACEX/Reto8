from psycopg2 import connect

class Connection:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = connect(host='127.0.0.1',
                    user='postgres', 
                    password='ALANICK1985$', 
                    database='biblioteca')
        self.cursor = self.db.cursor()

    def execute_query(self, query): # Se usa para ejecutar INSERT, UPDATE, DELETE (DDL)
        self.cursor.execute(query)
        self.commit()

    def get_all(self, order):
        query = f'SELECT * FROM {self.table_name} ORDER BY {order}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(self, id_object):
        query = f'''
            SELECT * FROM {self.table_name} WHERE 
            {"".join(map(str, id_object.keys()))} = {"".join(map(str, id_object.values()))}
        '''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_columns(self, id_object):
        list_where = []
        for field_name, field_value in id_object.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_where.append(f"{field_name}={value}")
        query = f'''
            SELECT * FROM {self.table_name} WHERE {" AND ".join(list_where)}
        '''
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, data):
        values = "'" + "', '".join(map(str, data.values())) + "'"
        query = f'INSERT INTO {self.table_name} ({", ".join(data.keys())}) VALUES ({values})'
        self.execute_query(query)
        return True

    def update(self, id_object, data):
        list_update = []
        for field_name, field_value in data.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_update.append(f"{field_name}={value}")

        list_where = []
        for field_name, field_value in id_object.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_where.append(f"{field_name}={value}")

        query = f'''
            UPDATE {self.table_name} SET {", ".join(list_update)} 
            WHERE 
            {" AND ".join(list_where)}
        '''
        self.execute_query(query)
        return True

    def delete(self, id_object):
        list_where = []
        for field_name, field_value in id_object.items():
            value = field_value
            if isinstance(field_value, str):
                value = f"'{field_value}'"
            list_where.append(f"{field_name}={value}")

        query = f'''
            DELETE FROM {self.table_name}
            WHERE 
            {" AND ".join(list_where)}
        '''
        self.execute_query(query)
        return True

    def commit(self):
        self.db.commit()
        return True
