from regla_validacion import ReglaValidacion

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = {'@', '_', '#', '$', '%'}
        return any(c in caracteres_especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise ValueError("La clave debe tener más de 8 caracteres.")
        if not self._contiene_mayuscula(clave):
            raise ValueError("La clave debe contener al menos una letra mayúscula.")
        if not self._contiene_minuscula(clave):
            raise ValueError("La clave debe contener al menos una letra minúscula.")
        if not self._contiene_numero(clave):
            raise ValueError("La clave debe contener al menos un número.")
        if not self.contiene_caracter_especial(clave):
            raise ValueError("La clave debe contener al menos un carácter especial (@, _, #, $, %).")
        return True