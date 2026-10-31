# Projeto Final - Unidade 2 - Cálculo Numérico (UNIVASF 2026.2)

Repositório da **Equipe 14** referente à Atividade Complementar da Unidade 2.
* **Data da Apresentação em Sala:** 19/11/2026 (Turma 02)
* **Entrega Final no Amadeus (Código + Relatório):** 20/11/2026 às 23:59
* **Prazo Interno da Equipe para juntar na `main`:** 14/11/2026

## Questões Sorteadas da Equipe 14
1. **Questão 01.3 (Tópico 01 - Métodos Diretos):** Cálculo do volume minerado em 3 minas (Areia, Cascalho Fino e Cascalho Grosso) usando Eliminação de Gauss.
2. **Questão 02.3 (Tópico 02 - Métodos Iterativos):** Cálculo das 5 correntes de malha de um circuito elétrico usando o Método de Gauss-Seidel (aproximação inicial `bi/aii` e precisão `0.0001`).
3. **Questão 03.2 (Tópico 03 - Interpolação Polinomial):** Estimativa da queda de tensão `V` para `i = 1.15 A` usando Interpolação de Lagrange e de Newton (2º, 3º e 4º graus).
4. **Questão 04.2 (Tópico 04 - Integração Numérica):** Cálculo da área da superfície de um rio no intervalo `[0, 40]` usando as Regras do Trapézio Repetida e de Simpson 1/3 Repetida.

## Divisão das Partes no Código (`main.py`)

| Integrante | Parte Responsável | O que deve implementar |
| :--- | :--- | :--- |
| **João Emanuel Almeida Ramos** | **1ª PARTE:** Sistemas Lineares (`01.3` e `02.3`) | Funções `eliminacao_gauss(A, b)` e `gauss_seidel(A, b, tol)` |
| **Júlio César Mendes do Nascimento** | **2ª PARTE:** Integração Numérica (`04.2`) + Menu Principal | Funções `regra_trapezio_repetida`, `regra_simpson_repetida`, validação de entradas e menus das Questões `01.3`, `02.3` e `04.2` |
| **Eduardo dos Santos Ferreira Sousa** | **3ª PARTE:** Interpolação Polinomial (`03.2` Completa) | Funções `interpolacao_lagrange`, `interpolacao_newton` e a tela interativa `menu_questao_03_2()` da Opção 3 |

## Como começar a programar
1. Crie a sua branch (ou abra o Codespace) e programe apenas dentro do bloco da sua parte no `main.py`.
2. Cada parte é independente: a 3ª Parte (Questão `03.2`) é chamada diretamente quando o usuário escolhe a Opção 3 no menu.
3. Para testar no terminal, execute:
```bash
python main.py

