def diferenciaSimetrica(lista_A, lista_B):
    """
    Computes the symmetric difference between two sets.
    The symmetric difference of two sets is the set of elements that are
    in either of the sets but not in their intersection. This function
    uses the '^' operator to achieve this.
    Parameters:
    lista_A (set): The first input set.
    lista_B (set): The second input set.
    Returns:
    set: A set containing the elements that are in either lista_A or lista_B
          but not in both, representing the symmetric difference.
    """
    resultado = lista_A ^ lista_B  # Compute the symmetric difference using the '^' operator

    return resultado

def main():

    conjunto_A = {"Juan", "Carlos", "Pedro", 4}
    conjunto_B = {"Juan", 4, 5, 2}

    resultado = diferenciaSimetrica(conjunto_A, conjunto_B)

    print("La diferencia simetria entre A y B es :", resultado)

main()