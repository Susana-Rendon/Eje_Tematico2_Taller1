# Pedimos al usuario que ingrese una palabra o frase
frase = input("Ingresa una palabra o frase: ").lower()

# Inicializamos las vocales que queremos contar
vocales = "aeiou"

for vocal in vocales:
    cantidad = frase.count(vocal)
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")
