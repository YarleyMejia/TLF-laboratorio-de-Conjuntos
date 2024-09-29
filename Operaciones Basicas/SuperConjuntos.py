def es_superconjuntoCaso1(A, B):
    """
    Checks if list A is a superset of list B.
    This function iterates through each element in list B and checks if it is present in list A.
    If any element from B is not found in A, the function returns False.
    If all elements from B are found in A, it returns True.
    Parameters:
    A (list): The first list to be checked.
    B (list): The second list to check against the first.
    Returns:
    bool: True if A is a superset of B; otherwise, False.
    """
    for elemento in B:
        if elemento not in A:
            return False
    return True


def es_superconjuntoCaso2(A, B):
    """
    Checks if list A is a superset of list B with an additional length condition.
    This function first checks if the length of A is less than or equal to the length of B.
    If so, it returns False, since a superset must be at least as large as the subset.
    If the length condition is met, it calls es_superconjuntoCaso1 to determine if A is a superset of B.
    Parameters:
    A (list): The first list to be checked.
    B (list): The second list to check against the first.
    Returns:
    bool: True if A is a superset of B; otherwise, False.
    """
    if len(A) <= len(B):
        return False
    return es_superconjuntoCaso1(A, B)

def main():
    A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    B = {1, 2, 3, 4, 5}

    print(f"Conjunto A: {A}\nConjunto B: {B}\n")
    print("¿A es superconjunto de B?\n")

    es_superconjunto1_A_B = es_superconjuntoCaso1(A, B)
    print("Utilizando función es_superconjuntoCaso1():", es_superconjunto1_A_B)


    es_superconjunto2_A_B = es_superconjuntoCaso2(A, B)
    print("Utilizando función es_superconjuntoCaso2():", es_superconjunto2_A_B)


main()