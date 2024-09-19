def diferencia(conjuntoA, conjuntoB):
    resultado= conjuntoA-conjuntoB

    return resultado;
def main():

    conjunto_A = {"Juan", "Carlos", "Pedro", 4}
    conjunto_B = {"Juan", 4, 5, 2}

    resultado = diferencia(conjunto_A, conjunto_B)

    print("Diferencia de A - B:", resultado)

main()