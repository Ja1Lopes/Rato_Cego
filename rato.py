from sympy import *

x, e, k = symbols("x e k")

half = Rational(1, 2)
third = Rational(1, 3)

Tfrac = Matrix(
    [
        [0, half, 0, half, 0],
        [half, 0, third, 0, 0],
        [0, half, 0, half, 0],
        [half, 0, third, 0, 0],
        [0, 0, third, 0, 1],
    ]
)

T = Matrix(
    [
        [0, 0.5, 0, 0.5, 0],
        [0.5, 0, 0.33, 0, 0],
        [0, 0.5, 0, 0.5, 0],
        [0.5, 0, 0.33, 0, 0],
        [0, 0, 0.33, 0, 1],
    ]
)


def prob_teste():
    y = []
    for j in range(0, 4):
        ej = Matrix([[0], [0], [0], [0], [0]])
        ej[j] = 1
        a = (T**10) * ej

        y.append(a.evalf(2))

        print(f"Testando coluna {j + 1} \n")
        pprint([a.evalf(2), ej])


def probability_to_find_cheese(k):
    P, D = T.diagonalize()

    P_k = P * (D**k) * (P**-1)

    return P_k.evalf(2)


def main():
    init_printing(wrap_line=False)
    print("\n Matriz probabilidade: \n")
    pprint(Tfrac)
    print("\n")

    prob_teste()

    k = 1000
    print("\n")
    print(f"Matriz resposta de C com k = {k}: \n")
    pprint(probability_to_find_cheese(k))
    print("\n")

    print(
        """
    Considerações finais:
            a) A posição P55 de T é igual a 1 pois o rato já está na sala e não sairá de lá, por este mesmo motivo Pi5 = 0 pois o rato uma vez chegando a sala 5 não sairá mais de lá.

            b) A maior probabilidade é j = 3 e a menor é j = 1, era o esperado pois com a disposição das salas a chance em j = 3 é muito maior, já j = 2 ou 4 é a mesma e por ser mais distante, j = 1 é a menor(Fórmula usada: T**10 * ej).

            c) Como demonstrado pela matriz apresentada na letra "C", conforme k tende ao infinito, a probabilidade do rato chegar à quinta sala e achar o queijo converge a 1 (caso desejável, pode-se trocar o valor para mostrar diferentes resultados, Fórmula usada: T^k = P * D**k * P**-1).
          """
    )
    if input():
        exit()


if __name__ == "__main__":
    main()
