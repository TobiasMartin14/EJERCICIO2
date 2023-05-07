from claseViajero import Viajero
from controladorViajeros import Controlador
from claseMenu import Menu

if __name__ == "__main__":
    viajeros = Controlador()
    viajeros.cargarDatos()
    numViajero = int(input("Ingrese un numero de viajero: "))
    viajero = viajeros.buscar_viajero(numViajero)
    menu = Menu()
    menu.opciones(viajero)