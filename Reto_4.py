import json

catalogo = json.loads(input("Ingrese Catalogo: "))
secGenOrd = "".join(sorted(input("Secuencia Genes: ")))

valor = 1
indice = 1
genes = ""
cantidad = ""
genPersona = {}
total = 0
genDis = ""

for i in secGenOrd:
    if indice != len(secGenOrd) and i == secGenOrd[indice]:
        valor += 1
    else:
        genes += i
        cantidad += str(valor)
        genPersona[i] = valor
        valor = 1
    indice += 1

for cat in catalogo:
    for gp in genPersona:
        if cat == gp:
            vrGen = catalogo[cat] * genPersona[gp]
            total += vrGen
            genDis += str(cat)

print(total)
print(genDis)
