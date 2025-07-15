# Trabalhos Compiladores

* Ana Ellen Deodato da Silva, 800206
* Gabriel Vianna Spolon, 811649
* Vinicius Gonçalves Perillo, 800219

# Simplifying Latex Equations

## Descrição

Este projeto converte expressões matemáticas em notação simplificada (ex: `raiz{x}`, `lim[x->0]`, `int[a to b]{f x dx}`) para expressões válidas em **LaTeX** (ex: `\sqrt{x}`, `\lim_{x \to 0}`, `\int_{a}^{b} f x\,dx`).

## Tabela de Conversões: Pseudoexpressões Matemáticas → LaTeX

| Nome                         | Função/Expressão (entrada)                                                                                                 | LaTeX esperado (saída)                                                                                           |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Binômio de Newton            | `$$ (a+b)(c-e) = a^2 + b^2 $$`                                                                                             | `\displaystyle (a+b)(c-e) = a^{2} + b^{2}`                                                                      |
| Identidade Trigonométrica     | `$$ sin^2theta + cos^2theta = 1 $$`                                                                                        | `\sin^{2} \theta + \cos^{2} \theta = 1`                                                                          |
| Série Aritmética             | `$$ sum[i=1 to n] i = {n(n+1)/2} $$`                                                                                       | `\sum_{i=1}^{n} i = \frac{n (n+1)}{2}`                                                                            |
| Série Fatorial               | `$$ prod[i=1 to n] i = n! $$`                                                                                              | `\prod_{i=1}^{n} i = n!`                                                                                          |
| Limite Notável 1             | `$$ lim[x->0]{{sin x/x}} = 1 $$`                                                                                           | `\lim_{x \to 0} \frac{\sin x}{x} = 1`                                                                             |
| Limite Notável 2             | `$$ lim[n->inf]{(1 + {1/n})^n} = e $$`                                                                                      | `\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{n} = e`                                                       |
| Teorema Fundamental do Cálculo| `$$ int[a to b] {der[x] f(x)} dx = f(b) - f(a) $$`                                                                         | `\int_{a}^{b} \frac{d f(x)}{dx} \, dx = f(b) - f(a)`                                                             |
| Entropia de Boltzmann        | `$$ S = k log W $$`                                                                                                        | `S = k \log W`                                                                                                    |
| Lei de Coulomb               | `$$ F = {k |q_1 q_2| / r^2} $$`                                                                                            | `F = \frac{k |q_1 q_2|}{r^{2}}`                                                                                   |
| Equação de Onda              | `$$ pder^2[t^2] u = c^2 nabla^2 u $$`                                                                                      | `\frac{\partial^{2} u}{\partial t^{2}} = c^{2} \nabla^{2} u`                                                     |
| Fórmula de Bhaskara          | `$$ @delt <- sqrt{b^2 - 4ac} $$`                                                                                          | `\delta \leftarrow \sqrt{b^{2} - 4 a c}`                                                                          |
|                              | `$$ x = {-b +- @delt/2a} $$`                                                                                              | `x = \frac{-b \pm \delta}{2 a}`                                                                                   |
| Correlação de Pearson        | `$$ rho = {nsum{xy} - sum{x}sum{y}/sqrt{(sum{x^2} - (sumx)^2)(sumy^2 - (sumy)^2)}} $$`                                       | `\rho = \frac{\mathrm{nsum} (x y) - \sum x \sum y}{\sqrt{\left(\sum x^{2} - (\sum x)^{2}\right)\left(\sum y^{2} - (\sum y)^{2}\right)}}` |
| Expressão extra 1            | `$$ @int <- e^x $$`                                                                                                        | `\text{@int} \leftarrow e^{x}`                                                                                     |
| Integral com variável definida| `$$ int[a to b] {@int} dx = @int $$`                                                                                       | `\int_{a}^{b} \text{@int} \, dx = \text{@int}`                                                                    |
| Outra expressão Lei de Coulomb| `$$ F = {k |q_1 q_2| / r^2} $$`                                                                                            | `F = \frac{k |q_1 q_2|}{r^{2}}`                                                                                   |
| Variável Delta com raiz       | `$$ @delt <- sqrt{b^2 - 4ac} $$`                                                                                          | `\delta \leftarrow \sqrt{b^{2} - 4 a c}`                                                                          |
| Fórmula Bhaskara com delta    | `$$ x = {-b +- @delt/2a} $$`                                                                                              | `x = \frac{-b \pm \delta}{2 a}`                                                                                   |
| Fórmula Bhaskara com delta typo| `$$ x = {-b +- @delta/2a} $$`                                                                                             | `x = \frac{-b \pm \text{@delta}}{2 a}`                                                                             |
| Correlação de Pearson (repetida) | `$$ rho = {nsum{xy} - sum{x}sum{y}/sqrt{(sum{x^2} - (sumx)^2)(sumy^2 - (sumy)^2)}} $$`                                     | `\rho = \frac{\mathrm{nsum} (x y) - \sum x \sum y}{\sqrt{\left(\sum x^{2} - (\sum x)^{2}\right)\left(\sum y^{2} - (\sum y)^{2}\right)}}` |


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
> python main.py teste.txt saida.tex

para transformar o modelo na nossa linguagem para LateX.

Ou para converter arquivos .md em massa:

> python main2.py Conversor/entrada Conversor/saida

4. Execute: 
> pip install pdf2image

ou

> sudo apt-get install poppler-utils