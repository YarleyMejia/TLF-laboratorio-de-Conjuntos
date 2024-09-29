def union_listas(lista_A, lista_B):
    """
    Returns the union of two lists, eliminating duplicates.
    The function takes two lists as input and creates a new list that contains all the elements from both lists,
    without duplicating any elements.
    Parameters:
    lista_A (list): The first list of elements.
    lista_B (list): The second list of elements.
    Returns:
    list: A list containing the union of the elements from lista_A and lista_B, without duplicate elements.
    """
    union = []
    for elemento in lista_A:
        if elemento not in union:
            union.append(elemento)
    for elemento in lista_B:
        if elemento not in union:
            union.append(elemento)
    return union



def main():

    conjunto_A = ["a", "b", "c"]
    conjunto_B = ["c", 4, 5]

    resultado_union = union_listas(conjunto_A, conjunto_B)

    print("Unión de A y B:", resultado_union)

main()