"""
PROJETO FINAL - UNIDADE 2 - CÁLCULO NUMÉRICO (UNIVASF 2026.2)
EQUIPE 14 - QUESTÕES: 01.3, 02.3, 03.2 e 04.2

Divisão de Tarefas:
- 1ª PARTE (João Emanuel): Sistemas Lineares (01.3 e 02.3)
- 2ª PARTE (Júlio César): Integração Numérica (04.2) e Menus das Opções 1, 2 e 4
- 3ª PARTE (Eduardo dos Santos): Interpolação Polinomial Completa (03.2)
"""


# ==============================================================================
# DADOS OFICIAIS DAS QUESTÕES SORTEADAS DA EQUIPE 14 
# ==============================================================================

def dados_questao_01_3():
    """Questão 01.3: Matriz de composição das 3 minas e demandas."""
    A = [
        [0.55, 0.25, 0.25],
        [0.30, 0.45, 0.20],
        [0.15, 0.30, 0.55]
    ]
    b = [4800.0, 5800.0, 5700.0]
    return A, b


def dados_questao_02_3():
    """Questão 02.3: Circuito de 5 malhas e precisão de 0.0001."""
    A = [
        [ 9.5, -2.5,  0.0, -2.0,  0.0],
        [-2.5, 11.0, -3.5,  0.0, -5.0],
        [ 0.0, -3.5, 15.5,  0.0, -4.0],
        [-2.0,  0.0,  0.0,  7.0, -3.0],
        [ 0.0, -5.0, -4.0, -3.0, 12.0]
    ]
    b = [12.0, -16.0, 14.0, 10.0, -30.0]
    tol = 0.0001
    return A, b, tol


def dados_questao_03_2():
    """Questão 03.2: Tabela de corrente vs tensão para estimar i = 1.15 A."""
    i_pontos = [0.25, 0.75, 1.25, 1.50, 2.00]
    v_pontos = [-0.45, -0.60, 0.70, 1.88, 6.00]
    i_alvo = 1.15
    return i_pontos, v_pontos, i_alvo


def dados_questao_04_2():
    """Questão 04.2: Margens M1 e M2 do rio no intervalo [0, 40] e passo h = 10."""
    x = [0.0, 10.0, 20.0, 30.0, 40.0]
    m1 = [50.8, 86.2, 136.0, 72.8, 51.0]
    m2 = [113.6, 144.5, 185.0, 171.2, 95.3]
    larguras = [m2[k] - m1[k] for k in range(len(x))]
    h = 10.0
    return x, m1, m2, larguras, h


# ==============================================================================
# 1ª PARTE: SISTEMAS LINEARES - QUESTÕES 01.3 E 02.3 (João Emanuel)
# ==============================================================================

def eliminacao_gauss(A: list, b: list) -> list:
    n = len(b)
    M = [linha[:] + [float(b[i])] for i, linha in enumerate(A)]

    for k in range(n):
        linha_pivo = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[linha_pivo][k]) < 1e-12:
            raise ValueError("Sistema singular ou sem solucao unica.")

        if linha_pivo != k:
            M[k], M[linha_pivo] = M[linha_pivo], M[k]

        for i in range(k + 1, n):
            fator = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= fator * M[k][j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - soma) / M[i][i]

    return x


def gauss_seidel(A: list, b: list, tol: float = 0.0001, max_iter: int = 1000) -> dict:
    pass


# ==============================================================================
# 2ª PARTE: INTEGRAÇÃO (04.2) E MENUS DAS OPÇÕES 1, 2 E 4 (Júlio César)
# ==============================================================================

def regra_trapezio_repetida(h: float, y: list) -> float:
    pass


def regra_simpson_repetida(h: float, y: list) -> float:
    pass


def menu_questao_01_3():
    pass


def menu_questao_02_3():
    pass


def menu_questao_04_2():
    pass


# ==============================================================================
# 3ª PARTE: INTERPOLAÇÃO POLINOMIAL - QUESTÃO 03.2 COMPLETA (Eduardo dos Santos)
# ==============================================================================

def selecionar_pontos_proximos(x_todos: list, y_todos: list, x_alvo: float, grau: int):
    pass


def interpolacao_lagrange(x_base: list, y_base: list, x_alvo: float) -> float:
    pass


def interpolacao_newton(x_base: list, y_base: list, x_alvo: float) -> float:
    pass


def menu_questao_03_2():
    pass


# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================

def exibir_menu():
    print("\n" + "=" * 60)
    print("   PROJETO FINAL UNIDADE 2 - CÁLCULO NUMÉRICO (EQUIPE 14)")
    print("=" * 60)
    print("1 - Questão 01.3: Sistemas Lineares - Eliminação de Gauss (3 Minas)")
    print("2 - Questão 02.3: Sistemas Lineares - Gauss-Seidel (Circuito)")
    print("3 - Questão 03.2: Interpolação de Lagrange e Newton (Resistor)")
    print("4 - Questão 04.2: Integração - Trapézio e Simpson (Área do Rio)")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_questao_01_3()
        elif opcao == "2":
            menu_questao_02_3()
        elif opcao == "3":
            menu_questao_03_2()
        elif opcao == "4":
            menu_questao_04_2()
        elif opcao == "0":
            print("\nEncerrando o programa.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
