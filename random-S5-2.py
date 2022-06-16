cliente = {
    'nombre': 0,
    'apellido': 0,
    'edad': 0,
    'producto': [],
}

nombre = input('¿Cuál es tu nombre? ')
cliente['nombre'] = nombre

apellido = input('¿Y tu apellido? ')
cliente['apellido'] = apellido

edad = int(input('¿Y tu edad? '))
cliente['edad'] = edad

producto = input('¿Qué producto deseas? ')
cliente['producto'] = producto

print('- Resumen de Compra: ',cliente)