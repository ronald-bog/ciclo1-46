secNatural = input("Secuencia Tratamiento Natural: ")
secTradicional = input("Secuencia Tratamiento Tradicional: ")
secCuerpo = input("Secuencia Genes que deberia generar el cuerpo: ")
pNatural = 0
pTradicional = 0
indice = 0
resultado = ""

for genes in secCuerpo:
    if secNatural[indice] == secTradicional[indice] and secCuerpo[indice] == genes:
        pNatural += +1
        pTradicional += +1
    elif secNatural[indice] == genes:
        pNatural += +1
    elif secTradicional[indice] == genes:
        pTradicional += +1
    if pNatural == pTradicional:
        resultado += "E"
    elif pNatural > pTradicional:
        resultado += "N"
    else:
        resultado += "T"
    indice += 1
print(resultado)
