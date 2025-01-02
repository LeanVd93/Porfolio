class Menu():
    def __init__(self) -> None:
        pass

    def crear_dicc(self):
        self.cantidad = int(input("Ingrese la cantidad de diccionarios que desea: "))
        self.menu = {f"Menu_{i+1}": {} for i in range(self.cantidad)}
        return self.menu

Prueba = Menu()
los = Prueba.crear_dicc()

print(los)
