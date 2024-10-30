from regla_validacion import ReglaValidacion

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave: str) -> bool:
        # Ejemplo de validación específica
        return "calisto" in clave.lower()

    def es_valida(self, clave: str) -> bool:
        return (self._validar_longitud(clave) and
                self.contiene_calisto(clave) and
                self._contiene_mayuscula(clave) and
                self._contiene_minuscula(clave) and
                self._contiene_numero(clave))

