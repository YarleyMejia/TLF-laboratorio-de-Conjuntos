def diferencia(conjuntoA, conjuntoB):
    """
    Computes the difference between two sets.
    The difference of two sets, A and B, is the set of elements that
    are in A but not in B. This function uses the '-' operator to
    achieve this.
    Parameters:
    conjuntoA (set): The first input set (from which elements are taken).
    conjuntoB (set): The second input set (from which elements are excluded).
    Returns:
    set: A set containing the elements that are in conjuntoA but not in conjuntoB.
    """

    resultado = conjuntoA - conjuntoB

    return resultado

def main():

    conjunto_A = {"Juan", "Carlos", "Pedro", 4}
    conjunto_B = {"Juan", 4, 5, 2}

    resultado = diferencia(conjunto_A, conjunto_B)

    print("Diferencia de A - B:", resultado)

main()