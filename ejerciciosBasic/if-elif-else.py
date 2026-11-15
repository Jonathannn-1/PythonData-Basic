## crear un programa que evalue la nota inbgresaada por un alumno

nota = int(input('Ingrese su nota:'))

if nota >= 90:
    print(f'Excelente tu nota es de A+')
elif nota >= 80:
    print(f'Excelente tu nota es A')
elif nota >= 70:
    print(f'Tu nota es de B+ intermedia')
elif nota >= 60:
    print(f'Tu nota es C Basica')
else:
    print('Has perdido la materia, sigue estudiando.')


##crear un programa que identifique si eres senior o junior

salario = int(input('Ingrese sus salario neto en dolares: '))
experiencia = int(input('Ingrese su experiencia en años: '))

if salario >= 3000:
    if experiencia >= 3:
        print('Felicidades eres senior')
else:
    print('Eres junior, debes seguir estudiando')


#$# operador IF ternario

categoria = 'sr' if experiencia >= 3 and salario >= 3000 else 'nob'
print(f'{categoria}')

impuesto = 0.16 if salario > 50000 else 0.10
print(f'impuesto aplicado = {impuesto*100}')