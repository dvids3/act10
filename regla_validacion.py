
class ReglaValidacion():
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada

    
    def es_valida(self, clave: str) -> bool:
        self.clave = clave

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) == self.longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)