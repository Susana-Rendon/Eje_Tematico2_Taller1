lista_num = []
suma_pares = 0

while True:
    numeros = input("Ingresa un número (o escribe fin para terminar): ")
    if numeros.lower() == "fin":
        break

    numero = int(numeros)
    lista_num.append(int(numero))

    if numero % 2 == 0:
        suma_pares += numero

print("Resultado de la suma de pares es:", suma_pares)