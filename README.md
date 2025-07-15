# Trabalhos Compiladores

* Ana Ellen Deodato da Silva, 800206
* Gabriel Vianna Spolon, 811649
* Vinicius Gonçalves Perillo, 800219

# Simplifying Latex Equations

## Descrição

Este projeto converte expressões matemáticas em notação simplificada (ex: `raiz{x}`, `lim[x->0]`, `int[a to b]{f x dx}`) para expressões válidas em **LaTeX** (ex: `\sqrt{x}`, `\lim_{x \to 0}`, `\int_{a}^{b} f x\,dx`).

## Tabela de Conversões (alguns exemplos): Pseudoexpressões Matemáticas → LaTeX

| Nome                            | Entrada                                                                                      | Saída                                                                 |
|---------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Binomio de Newton              | $$ (a+b)(c-e) = a^2 + b^2 $$                                                                | $$\left(a+b\right)\left(c-e\right)=a^2+b^2$$                         |
| Identidade Trigonométrica      | $$ sin^2theta + cos^2theta = 1 $$                                                           | $$\sin^{2} \theta+\cos^{2} \theta=1$$                                |
| Série Aritimética              | $$ sum[i=1 to n] i = {n(n+1)/2} $$                                                          | $$\sum_{i=1}^{n} i=\frac{n\left(n+1\right)}{2}$$                     |
| Série Fatorial                 | $$ prod[i=1 to n] i = n! $$                                                                 | $$\prod_{i=1}^{n} i=n!$$                                             |
| Limite Notável (1)            | $$ lim[x->0]{{sin x/x}} = 1 $$                                                              | $$\lim_{x \to 0} (\frac{\sin x}{x})=1$$                              |
| Limite Notável (2)            | $$ lim[n->inf]{(1 + {1/n})^n} = e $$                                                        | $$\lim_{n \to \infty} (\left(1+\frac{1}{n}\right)^n)=e$$            |
| Entropia de Boltzmann         | $$ S = k log W $$                                                                           | $$S=k\log W$$                                                        |
| Equação de Onda               | $$ pder^2[t^2] u = c^2 nabla^2 u $$                                                         | $$\frac{\partial ^{2} u}{\partial t^{2}}=c^2\nabla^2u$$             |
| Fórmula de Bhaskara           | $$ @delt <- sqrt{b^2 - 4ac} $$ <br> $$ x = {-b +- @delt/2a} $$                              | $$x=\frac{-b\pm \sqrt{(b^2-4ac)}}{2a}$$                              |
| Correlação de Pearson         | $$ rho = {nsum{xy} - sum{x}sum{y}/sqrt{(sum{x^2} - (sumx)^2)(sumy^2 - (sumy)^2)}} $$        | $$\rho=\frac{n\sum (xy)-\sum (x)\sum (y)}{\sqrt{\left(\sum (x^2)-\left(\sum x\right)^2\right)\left(\sum y^2-\left(\sum y\right)^2\right)}}$$ |


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