cuerdasJug = input("Cuerdas asociadas a los sonidos determinados por el jugador: ").upper().replace(",", "")
valor = 1
indice = 1
cuerdas = ""
cantidad = ""

for i in cuerdasJug:
    if i == cuerdasJug[indice:indice + 1]:
        valor += 1
    else:
        cuerdas += i + " "
        cantidad += str(valor) + " "
        valor = 1
    indice += 1

print(cuerdas)
print(cantidad)
