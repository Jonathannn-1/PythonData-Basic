
"""Variante para data eng: Haz un conversor de salarios mensuales a anuales + impuestos aproximados (15%).
    Tarea para la comunidad en Skool"""

def calcular_salario_anual(salario_mensual,incluyeIVA=False, impuesto=0.15):
    """logica que calcula el salario anial"""
    
    if incluyeIVA:
        salario_mensual = salario_mensual /1.16 # ELIMINAMOS IVA

    salario_anual = salario_mensual * 12
    impuesto = salario_anual * impuesto 
    salario_neto = salario_anual - impuesto

    return salario_anual, impuesto, salario_neto

def calculo():    
    try:

        salario_mensual = float(input('Ingrese su salario mensual:'))
        respuestaIVA = input('En el salario ihnclute IVA? (SI/NO): ').strip().lower()
        incluyeIVA = respuestaIVA == 'si'

        salario_anual, impuesto, salario_neto = calcular_salario_anual(
            salario_mensual,
            incluyeIVA=incluyeIVA,
            impuesto=0.15
        )

        print('---------resultado----------')
        print(f'salario anual {salario_anual:.2f}')
        print(f'imuesto {impuesto:.2f}')
        print(f'salario neto {salario_neto:.2f}')

    except ValueError:
        print('ingrese un numero valido como salario')
