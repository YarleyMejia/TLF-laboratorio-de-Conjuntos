def diferenciaSimetrica(lista_A, lista_B):
    resultado= lista_A ^lista_B

    return resultado;
def main():

    conjunto_A = {"Juan", "Carlos", "Pedro", 4}
    conjunto_B = {"Juan", 4, 5, 2}

    resultado = diferenciaSimetrica(conjunto_A, conjunto_B)

    print("La diferencia simetria entre A y B es :", resultado)

main()