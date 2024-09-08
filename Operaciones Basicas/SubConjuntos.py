def generarSubconjuntos(conjunto):
    if len(conjunto) == 0:
        return [[]]
    primer_elemento1= conjunto[0]
    subconjuntosVacio = generarSubconjuntos(conjunto[1:])
    adicionarElemento = [[primer_elemento1] + subconjunto for subconjunto in subconjuntosVacio]

    return subconjuntosVacio + adicionarElemento;


def main():
    conjunto = ["Carlos", "Pedro", "Orlay", "Daniela", "Yovany", "Yarley"] #Este []garantiza el orden y este {} NO.


    resultado = generarSubconjuntos(conjunto)

    print("Subconjuntos de", conjunto, ":")
    for subconjunto in resultado:
        print(subconjunto)


main()