import json

catalogo = json.loads(input("Ingrese Catalogo: "))
secGenOrd = sorted(input("Secuencia Genes: "))

valor = 0
genes = ""

for key, value in catalogo.items():
    if key in secGenOrd:
        genes += str(key)
        valor += (secGenOrd.count(key) * value)

print(valor)
print(genes)
