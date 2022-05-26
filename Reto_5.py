def categorias(lista):
    catSR = []
    [catSR.append(i) for i in lista if i not in catSR]
    return catSR


def mefaltandelacategoria(lpf, lc, c):
    indices = []
    [indices.append(i) for i in lpf if lc[i] == c]
    return indices


def notengopaciente(ls, lp):
    indicesCP = []
    [indicesCP.append(i) for i in ls if i not in lp]
    return indicesCP


def puedecambiar(cs, cp):
    cantidad = []
    [cantidad.append(i) for i in cs if i in cp]
    return len(cantidad)
