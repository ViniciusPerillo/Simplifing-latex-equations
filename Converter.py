from md_equationsParser import md_equationsParser
from md_equationsLexer import md_equationsLexer

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from io import StringIO
import sys
import re


class ConverterVisitor(ParseTreeVisitor):

    def __init__(self):
        super().__init__()
        self.vars = {}
        self.errors = []

    def visitDocument(self, ctx: md_equationsParser.DocumentContext):
        # Primeira passada: processa e armazena variáveis
        for child in ctx.children:
            if isinstance(child, md_equationsParser.EquationBlockContext):
                if child.IDENT() and child.ATRIB():
                    self.visitEquationBlock(child)  # Apenas armazena

        # Segunda passada: processa expressões finais
        output = []
        for child in ctx.children:
            if isinstance(child, md_equationsParser.EquationBlockContext):
                if not (child.IDENT() and child.ATRIB()):
                    output.append(self.visitEquationBlock(child))
                    output.append('\n\n')
            else:
                    output.append(None)

        latex = ''.join(filter(None, output))

        if self.errors:
            msgs = '\n'.join(self.errors)
            return f"Erros de variáveis:\n{msgs}\n\n{latex}"
        else:
            return latex


    def visitBlock(self, ctx):
        return ''.join([t.getText() for t in ctx.children])
    

    def visitEquationBlock(self, ctx):
        if ctx.IDENT() and ctx.ATRIB():
            var_name = ctx.IDENT().getText()
            expr = self.visit(ctx.equation())

            if var_name in self.vars:
                line = ctx.IDENT().getSymbol().line
                self.errors.append(f"Linha {line}: Variável {var_name} já declarada")
            self.vars[var_name] = expr
            return f"Variável {var_name} já declarada"

        else:
            eq = self.visit(ctx.equation())
            return f'$${eq}$$'


    def visitEquation(self, ctx):
        parts = [self.visit(ctx.sub_equation(i)) for i in range(len(ctx.sub_equation()))]
        comps = [ctx.COMP(i).getText() for i in range(len(ctx.COMP()))]
        out = parts[0]
        for op, part in zip(comps, parts[1:]):
            out += op + part
        return out

    def visitSub_equation(self, ctx):
        result = self.visit(ctx.parcela(0))
        for i in range(1, len(ctx.parcela())):
            op_raw = ctx.operator(i - 1).getText()
            op = {
                '+-': r'\pm ',
                '*': r'\cdot ',
                '/': '/',
                '+': '+',
                '-': '-',
            }.get(op_raw, op_raw)
            right = self.visit(ctx.parcela(i))
            
            result += op + right
        return result

    def visitSub_equation_brac(self, ctx):
        if ctx.LPAREN():
            expr = self.visit(ctx.sub_equation())
            return f'\\left({expr}\\right)'
        
        if ctx.MOD():
            expr = self.visit(ctx.sub_equation())
            return f'\\left|{expr}\\right|'
        
        if ctx.LBRACE():
            expr = self.visit(ctx.sub_equation())
            return f'\\left\\{{{expr}\\right\\}}' 
        
        return self.visit(ctx.sub_equation())


    def visitParcela(self, ctx):
        return ''.join(self.visit(sf) for sf in ctx.sub_fator())

    def visitSub_fator(self, ctx):
        if ctx.SQRT():
            inner = self.visit(ctx.apply_func())
            return r'\sqrt{' + inner + '}'
        if ctx.POW():
            base = self.visit(ctx.apply_func())
            return '^' + base
        if ctx.SUBIND():
            base = self.visit(ctx.apply_func())
            return '_{' + base + '}'
        if ctx.FAT():
            f = self.visit(ctx.fator())
            return f + '!'
        if ctx.MINUS():
            f = self.visit(ctx.fator())
            return '-' + self.visit(ctx.fator())
        
        return self.visit(ctx.fator())

    def visitFator(self, ctx):
        if ctx.ICOG():
            val = ctx.ICOG().getText()
            # Lista dos símbolos que precisam de barra no LaTeX
            latex_symbols = {
                'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta',
                'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho',
                'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega',
                'infty', 'nabla', 'partial',  # outros especiais
            }
            if val in latex_symbols:
                return '\\' + val
            else:
                return val        
        if ctx.numero():
            return ctx.numero().getText()
        
        if ctx.div():
            return self.visit(ctx.div())
        
        if ctx.funcao():
            return self.visit(ctx.funcao())
        
        if ctx.sub_equation_brac():
            return self.visit(ctx.sub_equation_brac())
        
        if ctx.IDENT():
                name = ctx.IDENT().getText()
                if name.startswith('@'):
                    if name not in self.vars:
                        line = ctx.IDENT().getSymbol().line
                        self.errors.append(f"Linha {line}: Variável {name} não declarada")
                        return f"<ERRO: {name} não declarado>"
                    valor = self.vars[name]
                    return valor
                return name
        return ''
            
    def visitNumero(self, ctx):
        if ctx.INF():
            return '\\infty'
        return ctx.getText()

    def visitDiv(self, ctx):
        num = self.visit(ctx.sub_equation(0))
        den = self.visit(ctx.sub_equation(1))

        return f'\\frac{{{num}}}{{{den}}}'
    

    def visitFuncao(self, ctx):
        if ctx.derivada_parcial():
            return self.visit(ctx.derivada_parcial())
        
        if ctx.funcao_nao_exp():
            return self.visit(ctx.funcao_nao_exp())

        if ctx.funcao_exp():
            nome = self.visit(ctx.funcao_exp())

            expoente = ''
            if ctx.POW():
                expoente = f'^{{{self.visit(ctx.fator())}}}'

            argumento = self.visit(ctx.apply_func())
            return f'\\{nome}{expoente} {argumento}'

        return ''


    def visitFuncao_exp(self, ctx):
        raw = ctx.getText().lower()
        mapa = {
            "sin": "sin",
            "cos": "cos",
            "tan": "tan",
            "sec": "sec",
            "log": "log",
            "ln": "ln",
            "arcsin": "arcsin",
            "arccos": "arccos",
            "arctan": "arctan",
        }
        return mapa.get(raw, raw)

        
    def visitLimite(self, ctx):
        var = ctx.ICOG().getText()
        limite = self.visit(ctx.numero())
        corpo = self.visit(ctx.apply_func())
        return f'\\lim_{{{var} \\to {limite}}} {corpo}'


    def visitIntegral(self, ctx):
        if ctx.ATE():
            sub = self.visit(ctx.sub_equation(0))
            sup = self.visit(ctx.sub_equation(1))
            expr = self.visit(ctx.apply_func())
            var = ctx.ICOG().getText()
            return rf'\int_{{{sub}}}^{{{sup}}} {expr} \, d{var}'
        else:
            expr = self.visit(ctx.apply_func())
            var = ctx.ICOG().getText()
            return rf'\int {expr} \, d{var}'

    def visitDerivada(self, ctx):
        var = ctx.ICOG().getText()
        expr = self.visit(ctx.apply_func())
        return rf'\frac{{d{expr}}}{{d{var}}}'


    def visitDerivada_parcial(self, ctx):
        expoente_pder = ''
        fatores = ctx.getTypedRuleContexts(md_equationsParser.FatorContext)

        if ctx.POW() and len(fatores) >= 1:
            expoente_pder = '^{' + self.visit(fatores[0]) + '}'

        var = ctx.ICOG().getText()
        expoente_var = ''

        # Se tem expoente do var dentro dos colchetes
        if len(fatores) >= 2:
            expoente_var = '^{' + self.visit(fatores[1]) + '}'

        var_com_expoente = var + expoente_var
        argumento = self.visit(ctx.apply_func())

        return rf'\frac{{\partial {expoente_pder} {argumento}}}{{\partial {var_com_expoente}}}'



    def visitTorio(self, ctx):
        operador = '\\' + ctx.getChild(0).getText() 
        limites = ''
        if ctx.LBRACK():
            index_eq = self.visit(ctx.equation())
            sup = ''
            if ctx.ATE():
                sup = self.visit(ctx.sub_equation())
            limites = f'_{{{index_eq}}}'
            if sup:
                limites += f'^{{{sup}}}'

        argumento = self.visit(ctx.apply_func())
        return f'{operador}{limites} {argumento}'


    def visitApply_func(self, ctx):
        if ctx.fator():
            return self.visit(ctx.fator())
        
        inner = self.visit(ctx.sub_equation())
        if inner.startswith('\\left(') and inner.endswith('\\right)'):
            return inner 
        return f'({inner})'



    # padrão fallback
    def visitChildren(self, node):
        res = ''
        for c in node.getChildren():
            r = c.accept(self)
            if r: res += r
        return res

def convert(text:str):
    input_stream = InputStream(text)
    lexer = md_equationsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = md_equationsParser(stream)
    tree = parser.document()
    cv = ConverterVisitor()
    return cv.visit(tree)

if __name__ == '__main__':
    texto = sys.stdin.read()
    out = convert(texto)
    sys.stdout.write(out)
