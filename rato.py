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
    # Fórmula -> (P ** k) * P.col(j)
    y = []
    for j in range(0, 4):
        ej = Matrix([[0], [0], [0], [0], [0]])
        ej[j] = 1
        a = (T**10) * ej

        y.append(a.evalf(2))

        print(f"Testanto coluna {j + 1} \n")
        pprint([a.evalf(2), ej])


def infinite_Diagonal(matrix):
    for k in range(1, 100, 10):
        print(f"Limite de k -> +oo | k = {k}: \n")
        pprint((matrix**k).evalf(2))
        pprint(limit(matrix, k, oo, "+"))
        print("\n")


def main():
    init_printing(wrap_line=False)
    print("\n Matriz probabilidade: \n")
    pprint(Tfrac)
    print("\n")

    prob_teste()

    M, D = T.diagonalize()
    Diag = (D).evalf(2)

    print("\n T diagonalizada: \n")
    pprint(Tfrac)
    print("\n")

    infinite_Diagonal(T)

    if input():
        exit()


if __name__ == "__main__":
    main()
