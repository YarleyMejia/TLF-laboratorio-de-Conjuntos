def union_listas(lista_A, lista_B):
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