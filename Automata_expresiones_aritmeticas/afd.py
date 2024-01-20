from estado import Estado

class AutomataAritmetico:
    def __init__(self):
        # Crear instancias de estados
        estado_0 = Estado()
        estado_1 = Estado()
        estado_2 = Estado()
        estado_3 = Estado(es_final=True)

        # Definir transiciones
        for digito in '0123456789':
            estado_0.agregar_transicion(digito, estado_1)
            estado_1.agregar_transicion(digito, estado_1)
            estado_2.agregar_transicion(digito, estado_3)
            estado_3.agregar_transicion(digito, estado_3)
        for operador in '+-*/':
            estado_1.agregar_transicion(operador, estado_2)
            estado_3.agregar_transicion(operador, estado_2)

        # Establecer estado inicial
        self.estado_inicial = estado_0

    def validar_expresion_aritmetica(self, cadena):
        estado_actual = self.estado_inicial
        for caracter in cadena:
            if caracter not in estado_actual.transiciones:
                return False
            estado_actual = estado_actual.transiciones[caracter]
        return estado_actual.es_final
