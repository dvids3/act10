from regla_validacion import ReglaValidacion


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        mayusculas = sum(1 for c in clave if c in 'CALISTO')
        return mayusculas >= 2 and not clave.isupper()

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise ValueError("La clave debe tener más de 6 caracteres.")
        if not self._contiene_numero(clave):
            raise ValueError("La clave debe contener al menos un número.")
        if not self.contiene_calisto(clave):
            raise ValueError("La clave debe contener la palabra 'calisto' con al menos dos letras mayúsculas.")
        return True

