from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError("FUERA DE RANGO", ancho, self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto < 1 or alto > self.MAX:
            raise DimensionError("FUERA DE RANGO", alto, self.MAX)
        self.__alto = alto

f = Foto(0,0, "ruta")
#POR PANTALLA PIDE QUE COLOQUES NUEVO VALOR SI COLOCAS ALGUN NUMERO MAYOR AL MAXIMO QUE ESTA DELCRADO EN 2500 SALE EL ERROR
f.alto = int(input("Ingresa el nuevo valor: "))
