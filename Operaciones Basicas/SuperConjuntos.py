def es_superconjuntoCaso1(A, B):
    for elemento in B:
        if elemento not in A:
            return False
    return True

def es_superconjuntoCaso2(A, B):
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