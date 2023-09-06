from sympy import *

x, e, k = symbols("x e k")

half = Rational(1, 2)
third = Rational(1, 3)

Tfrac = Matrix(
    [
        [1, half, 0, half, 0],
        [half, 1, third, 0, 0],
        [0, half, 1, half, 0],
        [half, 0, third, 1, 0],
        [0, 0, third, 0, 1],
    ]
)

T = Matrix(
    [
        [1, 0.5, 0, 0.5, 0],
        [0.5, 1, 0.33, 0, 0],
        [0, 0.5, 1, 0.5, 0],
        [0.5, 0, 0.33, 1, 0],
        [0, 0, 0.33, 0, 1],
    ]
)


def prob_teste(j):
    # Fórmula -> (P ** k) * P.col(j)
    y = []
    for k in range(1, 11):
        a = (T**k) * T.col(j)

        y.append(a.evalf(2))

        if a[4, 0] > 1:
            print(f"    Coluna: {j + 1} : k = {k} \n")
            break


def infinite_Diagonal(matrix):
    for i in range(1, 1000000, 10000):
        print(f"Matriz diagonal elevada a {i}: \n")
        pprint((matrix**i).evalf(2))
        print("\n")


def main():
    init_printing(wrap_line=False)
    print("\n Matriz probabilidade: \n")
    pprint(Tfrac)
    print("\n")

    for j in range(0, 4):
        print(f"Testanto coluna {j + 1} \n")
        prob_teste(j)

    M, D = T.diagonalize()
    Diag = (D).evalf(2)

    print("\n T diagonalizada: \n")
    pprint(Diag)

    infinite_Diagonal(Diag)

    if input():
        exit()


if __name__ == "__main__":
    main()
