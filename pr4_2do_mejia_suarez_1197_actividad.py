# Crear un diccionario vacio
informacion_persona = {}

# Solicitar informacion al usuario
while True:
    print("\nEscribe 'salir' para finalizar.")
    
    clave = input("Introduce el dato (ej. nombre, edad, sexo): ").strip().lower()
    
    if clave == 'salir':
        break
    
    valor = input(f"Introduce el valor para {clave}: ").strip()
    
    # Añadir al diccionario
    informacion_persona[clave] = valor
    
    # Mostrar el contenido del diccionario
    print("\nContenido actual del diccionario:")
    print(informacion_persona)