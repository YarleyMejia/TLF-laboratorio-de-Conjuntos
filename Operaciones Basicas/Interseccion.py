def interseccion(conjuntoA, conjuntoB):
    """
    Computes the intersection of two sets.
    This function iterates through the elements of the first set (conjuntoA)
    and checks if each element is present in the second set (conjuntoB).
    If an element is found in both sets, it is added to the result list.
    Parameters:
    conjuntoA (list): The first input set.
    conjuntoB (list): The second input set.
    Returns:
    list: A list containing the elements that are present in both input sets,
          representing the intersection of the two sets.
    """
    resultado = []
    for elemento in conjuntoA:
        if elemento in conjuntoB:
            resultado.append(elemento)
    return resultado

def main():
    conjunto_A = ["Juan", "Carlos", "Pedro", 4]
    conjunto_B = ["Juan", 4, 5, 2]

    resultado = interseccion(conjunto_A, conjunto_B)

    print("Intersección de A y B:", resultado)

main()