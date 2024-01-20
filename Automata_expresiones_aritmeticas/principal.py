from afd import AutomataAritmetico

# Prueba
afd = AutomataAritmetico()
print(afd.validar_expresion_aritmetica('+3'))  # Debería imprimir: False
print(afd.validar_expresion_aritmetica('15+23'))  # Debería imprimir: True
print(afd.validar_expresion_aritmetica('17--7'))  # Debería imprimir: False
print(afd.validar_expresion_aritmetica('11+89'))  # Debería imprimir: True
print(afd.validar_expresion_aritmetica('345-17+'))  # Debería imprimir: False
print(afd.validar_expresion_aritmetica('786+809+443'))  # Debería imprimir: True
print(afd.validar_expresion_aritmetica('226*4/5-90+1'))  # Debería imprimir: True