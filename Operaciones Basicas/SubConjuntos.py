def generarSubconjuntos(conjunto):
    """
    Generates all possible subsets (the power set) of a given set.
    This function uses recursion to generate subsets. If the input set is empty, it returns a list containing an empty subset.
    For each element in the set, the function generates subsets that include and exclude that element.
    Parameters:
    conjunto (list): The input set from which subsets will be generated.
    Returns:
    list: A list of all possible subsets of the input set, including the empty set.
    """
    if len(conjunto) == 0:
        return [[]]
    primer_elemento1 = conjunto[0]
    subconjuntosVacio = generarSubconjuntos(conjunto[1:])
    adicionarElemento = [[primer_elemento1] + subconjunto for subconjunto in subconjuntosVacio]

    return subconjuntosVacio + adicionarElemento
def main():
    conjunto = ["Carlos", "Pedro", "Orlay", "Daniela", "Yovany", "Yarley"] #Este []garantiza el orden y este {} NO.


    resultado = generarSubconjuntos(conjunto)

    print("Subconjuntos de", conjunto, ":")
    for subconjunto in resultado:
        print(subconjunto)


main()