
from regla_validacion import ReglaValidacion
from ReglaValidacionCalisto import ReglaValidacionCalisto
from ReglaValidacionGanimedes import ReglaValidacionGanimedes

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)


try:
    validador_ganimedes = Validador(ReglaValidacionGanimedes())
    print(validador_ganimedes.es_valida("Ejemplo@1"))  

    validador_calisto = Validador(ReglaValidacionCalisto())
    print(validador_calisto.es_valida("cAliStO1"))  
except ValueError as e:
    print(e)