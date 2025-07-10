from md_equationsLexer import md_equationsLexer
from antlr4.error.ErrorListener import ErrorListener
from io import StringIO
import re

class LexerError(ErrorListener):
    '''
    Classe que herda ErrorListener para alaterar as mensagens de erro do lexer
    Inputs:
        output: StringIO -> arquivo IO que o print ira escrever
    '''
    def __init__(self, output: StringIO):
        super().__init__()
        self.out = output
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if '\\n' in msg or '\\r' in msg:
            if '{' in msg:
                print(f'Linha {line}: chaves não fechadas', file= self.out)
            elif '[' in msg:
                print(f'Linha {line}: colchetes não fechadas', file= self.out)
            elif '<!--' in msg:
                print(f'Linha {line}: comentario nao fechada', file= self.out)
        else:
            symbol = re.search(r"'(.*?)'", msg).group(1)
            print(f'Linha {line}: {symbol} - simbolo nao identificado', flush= True, file= self.out)

        print("Fim da compilacao", file=self.out)