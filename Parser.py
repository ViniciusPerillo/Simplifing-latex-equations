from md_equationsLexer import md_equationsLexer
from antlr4.error.ErrorListener import ErrorListener
from io import StringIO
import re

class InterromperParsing(Exception):
    pass

class ParserError(ErrorListener):
    '''
    Classe que herda ErrorListener para alaterar as mensagens de erro do parser
    Inputs:
        output: StringIO -> arquivo IO que o print ira escrever
    '''
    def __init__(self, output: StringIO):
        super().__init__()
        self.out = output
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(msg)
        # Trata o erro específico de EOF
        if 'EOF' in msg:
            print(f'Linha {line}: erro sintatico proximo a EOF', flush= True, file= self.out)
        elif 'inft' in msg:
            print(f'Linha {line}: Você não quis dizer inf?', flush= True, file= self.out)
        else:
            print(f'Linha {line}: erro sintatico proximo a {offendingSymbol.text}', flush= True, file= self.out)
