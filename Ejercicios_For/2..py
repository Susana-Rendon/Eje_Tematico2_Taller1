nombres = []

while True:
    nombre = input("Ingrese un nombre o escriba fin para terminar: ")
    if nombre.lower() == 'fin':
        break
    nombres.append(nombre)

nombres.sort()

print("Lista de nombres en orden alfabético:")
for nombre in nombres:
    print(nombre)