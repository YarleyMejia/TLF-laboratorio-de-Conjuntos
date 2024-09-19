def interseccion(conjuntoA, conjuntoB):
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