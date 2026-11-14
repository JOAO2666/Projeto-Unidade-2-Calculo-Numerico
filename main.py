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
    n = len(b)
    for i in range(n):
        if abs(A[i][i]) < 1e-12:
            raise ValueError("Diagonal principal contem elemento nulo.")

    x = [float(b[i]) / float(A[i][i]) for i in range(n)]
    x_inicial = x[:]

    erro_rel = float("inf")
    for k in range(1, max_iter + 1):
        x_ant = x[:]

        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / A[i][i]

        erro_abs = max(abs(x[i] - x_ant[i]) for i in range(n))
        max_x = max(abs(v) for v in x)
        erro_rel = erro_abs / max_x if max_x > 1e-12 else erro_abs

        if erro_abs < tol and erro_rel < tol:
            return {
                "x_inicial": x_inicial,
                "solucao": x,
                "iteracoes": k,
                "erro_rel": erro_rel,
                "convergiu": True
            }

    return {
        "x_inicial": x_inicial,
        "solucao": x,
        "iteracoes": max_iter,
        "erro_rel": erro_rel,
        "convergiu": False
    }


# ==============================================================================
# 2ª PARTE: INTEGRAÇÃO (04.2) E MENUS DAS OPÇÕES 1, 2 E 4 (Júlio César)
# ==============================================================================

def regra_trapezio_repetida(h: float, y: list) -> float:
    if(h <= 0 or len(y) < 2):
        raise ValueError("Informe uma passo positivo e pelo menos dois valores de y.")

    area_total = 0.0

    # Cada par de pontos consecutivos define um intervalo de integração 
    for i in range(len(y) - 1):
        area_trecho = (y[i] + y[i + 1]) * h / 2
        area_total = area_total + area_trecho

    return area_total


def regra_simpson_repetida(h: float, y: list) -> float:
    intervalos = len(y) - 1

    if (h <= 0 or intervalos < 2 or intervalos % 2 != 0):
        raise ValueError("Informe um passo positivo e um número par de intervalos (mínimo de 2).")

    area_total = 0.0

    # Cada grupo de três pontos corresponde a dois intervalos
    for i in range(0, intervalos, 2):
        area_trecho = (y[i] + 4 * y[i + 1] + y[i + 2]) * h / 3
        area_total = area_total + area_trecho

    return area_total

def ler_linha(mensagem: str, quantidade: int) -> list:
    texto = input(mensagem)
    partes = texto.split()

    #Cada equação precisa de um coeficiente apra cada incognita
    if len(partes) != quantidade:
        raise ValueError(f"Digite exatamente {quantidade} números separados por espaços.")

    linha = []
    for parte in partes:
        numero = float(parte)
        linha.append(numero)

    return linha

def ler_sistema():
    texto = input("Quantas incógnitas tem o sistema? ")
    ordem = int(texto)

    if ordem < 1:
        raise ValueError("A ordem do sistema deve ser pelo menos 1.")

    # Cada linha da matriz A contém os coeficientes de uma equação.
    A = []
    for i in range(ordem):
        linha = ler_linha(f"Coeficientes da equação {i + 1}: ", ordem)
        A.append(linha)

    b = ler_linha("Termos independentes, na ordem das equações: ", ordem)
    return A, b

def menu_questao_01_3():
    print("\nEliminação de Gauss")
    print("1 - Usar os dados das minas (questão 01.3)")
    print("2 - Informar outro sistema linear")
    print("0 - Voltar ao menu principal")

    opcao = input("Escolha uma opção: ").strip()
    if opcao == "0":
        return

    try:
        if opcao == "1":
            A, b = dados_questao_01_3()
        elif opcao == "2":
            A, b = ler_sistema()
        else:
            print("Opção inválida. Escolha 0, 1 ou 2.")
            return

        solucao = eliminacao_gauss(A, b)
    except ValueError as erro:
        print(erro)
        return

    for i in range(len(solucao)):
        if opcao == "1":
            print(f"Mina {i + 1}: {solucao[i]:.2f} m³")
        else:
            print(f"x{i + 1} = {solucao[i]}")

def menu_questao_02_3():
    print("\nMétodo de Gauss-Seidel")
    print("1 - Usar os dados do circuito (questão 02.3)")
    print("2 - Informar outro sistema linear")
    print("0 - Voltar ao menu principal")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "0":
        return

    try:
        if opcao == "1":
            A, b, tol = dados_questao_02_3()
        elif opcao == "2":
            A, b = ler_sistema()
            tol = float(input("Digite a tolerância (por exemplo, 0.0001): "))
            if tol <= 0:
                raise ValueError("A tolerância deve ser positiva.")
        else:
            print("Opção inválida. Escolha 0, 1 ou 2.")
            return

        # Os dois caminhos usam o mesmo método de cálculo.
        resultado = gauss_seidel(A, b, tol)
    except ValueError as erro:
        print(erro)
        return
    if resultado["convergiu"]:
        solucao = resultado["solucao"]
        for i in range(len(solucao)):
            if opcao == "1":
                print(f"I{i + 1} = {solucao[i]:.4f} A")
            else:
                print(f"x{i + 1} = {solucao[i]:.4f}")
    else:
        print("O método atingiu o limite de iterações sem convergir.")

def menu_questao_04_2():
    print("\nIntegração Numérica")
    print("1 - Usar os dados do rio (questão 04.2)")
    print("2 - Informar outra tabela de pontos")
    print("0 - Voltar ao menu principal")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "0":
        return
    elif opcao == "1":
        x, m1, m2, y, h = dados_questao_04_2()
    elif opcao == "2":
        # O passo h é a distância entre dois pontos consecutivos da tabela.
        try:
            texto_h = input("Digite o passo h (por exemplo, 0.5): ")
            h = float(texto_h)
            texto_y = input("Digite os valores de y separados: ")
            partes = texto_y.split()

            y = []
            for parte in partes:
                numero = float(parte)
                y.append(numero)
        
        except ValueError:
            print("Digite números válidos. Use ponto nos decimais e separe os valores de y")
            return
            
    else:
        print("Opção inválida. Escolha 0, 1 ou 2.")
        return

    try:
        area_trapezio = regra_trapezio_repetida(h, y)
        print("Integral pelo trapézio:", area_trapezio)

        area_simpson = regra_simpson_repetida(h, y)
        print("Integral por Simpson 1/3:", area_simpson)
    except ValueError as erro:
        print(erro)

# ==============================================================================
# 3ª PARTE: INTERPOLAÇÃO POLINOMIAL - QUESTÃO 03.2 COMPLETA (Eduardo dos Santos)
# ==============================================================================

def selecionar_pontos_proximos(x_todos: list, y_todos: list, x_alvo: float, grau: int):
    pass

def interpolacao_lagrange(x_base: list, y_base: list, x_alvo: float) -> float:
    n = len(x_base)
    y_resultado = 0.0
    for i in range(n):
        L = 1.0    
        for j in range(n):
            if i != j:
                numerador = x_alvo - x_base[j]
                denominador = x_base[i] - x_base[j]
                L = L * (numerador/denominador)

        y_resultado = y_resultado + (y_base[i] * L)    
        
    return y_resultado

def interpolacao_newton(x_base: list, y_base: list, x_alvo: float) -> float:
    pass


def menu_questao_03_2():
    grau = int(input("Defina o Grau do Polinomio: "))
    total_pontos = int(input("Define o total de pontos do Polinomio: "))
    x_alvo = float(input("Defina o Ponto que vai ser Alvo dentro da Função: "))
    lista_x = []
    lista_y = []

    for i in range(total_pontos):
        numero_x = float(input("Digite um número para a coordenada 'x': "))
        lista_x.append(numero_x)
    
    for j in range(total_pontos):
        numero_y = float(input("Digite um número para a coordenada 'y': "))
        lista_y.append(numero_y)

    selecionar_pontos_proximos(lista_x, lista_y, x_alvo, grau)



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
