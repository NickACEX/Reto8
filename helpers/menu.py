class Menu:
    def __init__(self, lista_menu):
        self.lista_menu=lista_menu

    def show(self):
        option=0
        print('Selecciona una opcion: \n')
        for x in range(0, len(self.lista_menu)):
            if x==len(self.lista_menu) -1:
                print(f'{str(x+1)}) {str(self.lista_menu[x])}\n')
            else:
                print(f'{str(x+1)}) {str(self.lista_menu[x])}')
        while True:
            try:
                option=int(input('>> '))
                if option in range(1, len(self.lista_menu)+1):
                    break
                else:
                    print('Debes ingresar un opcion valida')
            except ValueError:
                print('Debes ingresar un opcion valida')
        return option    