from prettytable import PrettyTable

def print_table(data, header=[]):
    tabla='Algo Ocurrio'
    if not data:
        raise ValueError('No hay dato para mostrar')
    if isinstance(data, list):
        if isinstance(data[0],dict):
            header=list(data[0].keys())
            tabla=PrettyTable(header)
            for row in data:
                tabla.add_row(list(row.values()))
        elif isinstance(data[0],tuple):
            header=table_header(data[0],header)
            tabla=PrettyTable(header)
            for row in data:
                tabla.add_row(list(row))
    elif isinstance(data, dict):
        header=list(data.keys())
        tabla=PrettyTable(header)
        tabla.add_row(list(data.values()))
    elif isinstance(data, tuple):
        header=table_header(data,header)
        tabla=PrettyTable(header)
        tabla.add_row(list(data))
    return tabla

def table_header(data, head):
    if not head:
        head=list(range(1, len(data)+1))   
    if len(head) < len(data):
        head.extend(list(range(len(head)+1,len(data)+1))) 
    if len(head) > len(data):
        del head[len(data):]
    return head

def question(text):
    print(f'\n{text}\n')
    option=False
    while True:
        dato=input('Seleccion (si) o (no) : ').strip() # si > SI 
        if dato.lower()=='si':
            option=True
            break
        if dato.lower()=='no':
            option=False
            break
        else:
            print('Debe elegir una opcion . . .')
    print('\n')
    return option

def input_data(text, tipo='string'):
    while True:
        try:
            if tipo=='string':
                data=input(text).strip()
            elif tipo=='int':
                data=int(input(text).strip())
            elif tipo=='float':
                data=float(input(text).strip())

            if str(data):
                if (isinstance(data, int) or isinstance(data, float)) and data < 0:
                    raise ValueError('') #raise se utiliza para retornar el error a los Except del Try & catch
                break
            else:
                print('No ingreso ningun dato')

        except ValueError:
            print('Debes de ingresar el Tipo de dato correcto')
   
    return data