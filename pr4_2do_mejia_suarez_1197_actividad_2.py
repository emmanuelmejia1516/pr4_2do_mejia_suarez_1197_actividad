print("Mejia Suarez Emmanuel Alexander_3w_1197")
# Crear el diccionario de traducción
entrada = input("Introduce palabras en formato 'español:inglés' separadas por comas: ")
diccionario = dict(par.split(":") for par in entrada.split(","))

# Pedir una frase en español
frase = input("Introduce una frase en español para traducir: ")

# Traducir palabra por palabra
traduccion = []
for palabra in frase.split():
    # Añadir la traducción si existe, si no, dejar la palabra igual
    traduccion.append(diccionario.get(palabra, palabra))

# Mostrar la frase traducida
print("Frase traducida:", ' '.join(traduccion))