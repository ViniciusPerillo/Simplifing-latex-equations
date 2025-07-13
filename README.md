# Trabalhos Compiladores

* Ana Ellen Deodato da Silva, 800206
* Gabriel Vianna Spolon, 811649
* Vinicius Gonçalves Perillo, 800219

# Simplifying Latex Equations

## Descrição

Este projeto converte expressões matemáticas em notação simplificada (ex: `raiz{x}`, `lim[x->0]`, `int[a to b]{f x dx}`) para expressões válidas em **LaTeX** (ex: `\sqrt{x}`, `\lim_{x \to 0}`, `\int_{a}^{b} f x\,dx`).

Tabela completa:

## Tabela de Conversões: Pseudoexpressões Matemáticas → LaTeX

| Entrada (Pseudo)                               | Saída (LaTeX)                                                                 |
|-----------------------------------------------|--------------------------------------------------------------------------------|
| raiz{a}                                        | \sqrt{a}                                                                       |
| {a}/{b}                                        | \frac{a}{b}                                                                    |
| case[x>0; x<0]{x}{-x}                          | \begin{cases} x, & \text{se } x \ge 0 \\ -x, & \text{se } x < 0 \end{cases}   |
| lim[x->0]                                      | \lim_{x \to 0}                                                                 |
| sin, cos, tan                                  | \sin, \cos, \tan                                                               |
| int[a; b]{fx dx}                               | \int_{a}^{b} fx \, dx                                                          |
| sum[n=1 to inf]{1}/{n^2}                       | \sum_{n=1}^{\infty} \frac{1}{n^2}                                              |
| der[x]{f}                                      | \dfrac{df}{dx}                                                                 |
| pder[x]{f}                                     | \dfrac{\partial f}{\partial x}                                                 |
| binom[a; b]                                    | \binom{a}{b}                                                                   |
| fat{a}                                         | a!                                                                             |
| union[A; B]                                    | A \cup B                                                                       |
| inter[A; B]                                    | A \cap B                                                                       |
| display{...}                                   | \displaystyle                                                                  |
| (a+b)!                                         | (a + b)!                                                                       |
| lim[x -> inf](1 + {1}/{x})^x                   | \lim_{x \to \infty} \left(1 + \frac{1}{x} \right)^x                            |
| x = {-b +- raiz(b^2 - 4ac)}/{2a}               | x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}                                         |
| int[-inf to x]{f(t) dt}                        | \int_{-\infty}^{x} f(t) \, dt                                                  |
| Cov(X, Y) = E[(X - {mu_X})(Y - {mu_Y})]        | \text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]                                   |
| A u B                                          | A \cup B                                                                       |
| A n B                                          | A \cap B                                                                       |
| A \ B                                          | A \setminus B                                                                  |
| N {c} Z {c} Q {c} R                            | \mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}           |
| for all x in R: x^2 >= 0                       | \forall x \in \mathbb{R},\ x^2 \ge 0                                           |
| exists x in R: x^2 = 2                         | \exists x \in \mathbb{R} \mid x^2 = 2                                          |
| not (P and Q) = not P or not Q                | \neg (P \land Q) \equiv \neg P \lor \neg Q                                    |
| p => q                                         | p \Rightarrow q                                                                |
| [[1, 2], [3, 4]]                               | \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}                                   |
| v = <x, y, z>                                  | \vec{v} = \langle x, y, z \rangle                                              |
| inv(A) = {1}/{det(A)} * adj(A)                 | A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)                                 |
| det([[a, b], [c, d]]) = ad - bc                | \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc                   |
| <u, v> = sum[i=1 to n] u_i * v_i               | \langle \vec{u}, \vec{v} \rangle = \sum_{i=1}^n u_i v_i                        |
| <a, b> = norm(a) * norm(b) * cos{theta}        | \vec{a} \cdot \vec{b} = |\vec{a}||\vec{b|\cos(\theta)                          |
| cross(a, b)                                    | \vec{a} \times \vec{b}                                                         |
| transpose(A)                                   | A^T                                                                            |

> ⚠️ Notação como `fat{a}`, `union[A; B]`, `display{}` são pseudo-funções da linguagem customizada e devem ser convertidas conforme a coluna “Saída (LaTeX)”.


## Arquivos principais

- `md_equationsLexer.g4` / `md_equationsParser.g4`: gramáticas ANTLR.
- `converter.py`: visitor que percorre a AST e gera LaTeX.
- `md_equationsLexer.py`, `md_equationsParser.py`: gerados pelo ANTLR.
- `lexer.py`, `parser.py`: definem os `ErrorListener` personalizados para tratamento de erros.
- `README.md`: instruções.

## Como usar

1. Gere os arquivos `md_equationsLexer.py` e `md_equationsParser.py`:
   ```bash
   antlr4 -Dlanguage=Python3 md_equationsLexer.g4
   antlr4 -Dlanguage=Python3 md_equationsParser.g4
