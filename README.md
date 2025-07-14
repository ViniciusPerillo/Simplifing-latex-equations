# Trabalhos Compiladores

* Ana Ellen Deodato da Silva, 800206
* Gabriel Vianna Spolon, 811649
* Vinicius Gonçalves Perillo, 800219

# Simplifying Latex Equations

## Descrição

Este projeto converte expressões matemáticas em notação simplificada (ex: `raiz{x}`, `lim[x->0]`, `int[a to b]{f x dx}`) para expressões válidas em **LaTeX** (ex: `\sqrt{x}`, `\lim_{x \to 0}`, `\int_{a}^{b} f x\,dx`).

## Tabela de Conversões: Pseudoexpressões Matemáticas → LaTeX

| Nome                    | Entrada (Pseudo)                               | Saída (LaTeX)                                                                 |
|-------------------------|------------------------------------------------|--------------------------------------------------------------------------------|
| Raiz quadrada           | raiz{a}                                        | \sqrt{a}                                                                       |
| Fração                  | {a}/{b}                                        | \frac{a}{b}                                                                    |
| Casos                   | case[x>0; x<0]{x}{-x}                          | \begin{cases} x, & \text{se } x \ge 0 \\ -x, & \text{se } x < 0 \end{cases}   |
| Limite                  | lim[x->0]                                      | \lim_{x \to 0}                                                                 |
| Funções trigonométricas| sin, cos, tan                                  | \sin, \cos, \tan                                                               |
| Integral definida       | int[a; b]{fx dx}                               | \int_{a}^{b} fx \, dx                                                          |
| Somatório infinito      | sum[n=1 to inf]{1}/{n^2}                       | \sum_{n=1}^{\infty} \frac{1}{n^2}                                              |
| Derivada                | der[x]{f}                                      | \dfrac{df}{dx}                                                                 |
| Derivada parcial        | pder[x]{f}                                     | \dfrac{\partial f}{\partial x}                                                 |
| Binomial                | binom[a; b]                                    | \binom{a}{b}                                                                   |
| Fatorial                | fat{a}                                         | a!                                                                             |
| União                   | union[A; B]                                    | A \cup B                                                                       |
| Interseção              | inter[A; B]                                    | A \cap B                                                                       |
| Exibição total          | display{...}                                   | \displaystyle                                                                  |
| Fatorial de soma        | (a+b)!                                         | (a + b)!                                                                       |
| Limite com infinito     | lim[x -> inf](1 + {1}/{x})^x                   | \lim_{x \to \infty} \left(1 + \frac{1}{x} \right)^x                            |
| Bhaskara simplificado   | x = {-b +- raiz(b^2 - 4ac)}/{2a}               | x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}                                         |
| Integral até x          | int[-inf to x]{f(t) dt}                        | \int_{-\infty}^{x} f(t) \, dt                                                  |
| Covariância             | Cov(X, Y) = E[(X - {mu_X})(Y - {mu_Y})]        | \text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]                                   |
| União simplificada      | A u B                                          | A \cup B                                                                       |
| Interseção simplificada | A n B                                          | A \cap B                                                                       |
| Diferença de conjuntos  | A \ B                                          | A \setminus B                                                                  |
| Inclusão de conjuntos   | N {c} Z {c} Q {c} R                            | \mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}           |
| Quantificador universal | for all x in R: x^2 >= 0                       | \forall x \in \mathbb{R},\ x^2 \ge 0                                           |
| Quantificador existencial| exists x in R: x^2 = 2                        | \exists x \in \mathbb{R} \mid x^2 = 2                                          |
| Lógica (negação)        | not (P and Q) = not P or not Q                | \neg (P \land Q) \equiv \neg P \lor \neg Q                                    |
| Implicação lógica       | p => q                                         | p \Rightarrow q                                                                |
| Matriz 2x2              | [[1, 2], [3, 4]]                               | \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}                                   |
| Vetor                   | v = <x, y, z>                                  | \vec{v} = \langle x, y, z \rangle                                              |
| Inversa de matriz       | inv(A) = {1}/{det(A)} * adj(A)                 | A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)                                 |
| Determinante 2x2        | det([[a, b], [c, d]]) = ad - bc                | \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc                   |
| Produto interno         | <u, v> = sum[i=1 to n] u_i * v_i               | \langle \vec{u}, \vec{v} \rangle = \sum_{i=1}^n u_i v_i                        |
| Produto escalar         | <a, b> = norm(a) * norm(b) * cos{theta}        | \vec{a} \cdot \vec{b} = |\vec{a}||\vec{b|\cos(\theta)                          |
| Produto vetorial        | cross(a, b)                                    | \vec{a} \times \vec{b}                                                         |
| Transposta de matriz    | transpose(A)                                   | A^T                                                                            |

> ⚠️ Notação como `fat{a}`, `union[A; B]`, `display{}` são pseudo-funções da linguagem customizada e devem ser convertidas conforme a coluna “Saída (LaTeX)”.


## Arquivos principais

- `md_equationsLexer.g4` / `md_equationsParser.g4`: gramáticas ANTLR.
- `converter.py`: visitor que percorre a AST e gera LaTeX.
- `md_equationsLexer.py`, `md_equationsParser.py`: gerados pelo ANTLR.
- `lexer.py`, `parser.py`: definem os `ErrorListener` personalizados para tratamento de erros.
- `README.md`: instruções.

## Como usar
1. Baixe o antlr e coloque na pasta com a Gramática e execute o comando:
>  python3 -m pip install antlr4-python3-runtime

2. Gere os arquivos `md_equationsLexer.py` e `md_equationsParser.py`:
> antlr4 -Dlanguage=Python3 md_equationsLexer.g4
> antlr4 -Dlanguage=Python3 md_equationsParser.g4

3. Execute: 
> python main.py casos_de_teste/entrada/teste_1.txt saida.tex

para transformar o modelo na nossa linguagem para LateX.

4. Execute: 
> pip install pdf2image

ou

> sudo apt-get install poppler-utils

para o Linux para transformar na imagem gerada pelo LateX.