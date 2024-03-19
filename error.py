
class DimensionError(Exception):
    def __init__(self, mensaje, dimension, maximo):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is not None and self.maximo is not None:
            return f"DimensionError: {self.dimension} Debiera estar entre 1 y {self.maximo}. Mensaje: {self.args[0]}"
        else:
            return super().__str__()