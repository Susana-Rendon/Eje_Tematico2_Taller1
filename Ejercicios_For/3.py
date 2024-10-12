lista_palabra = []

while True:
    palabra = input("Ingrese una palabra o ingrese fin para terminar: ")
    if palabra == "fin":
        break

    lista_palabra.append(palabra)

letra = input("Ingrese una letra por la que quiere que comience las palabras fin para terminar: ").lower()

print(f"Las palabras que comienzan con la letra: {letra}")

for palabra in lista_palabra:
    if palabra.lower().startswith(letra):
        print(palabra)
