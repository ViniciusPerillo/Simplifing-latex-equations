from io import StringIO
import sys
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from Lexer import LexerError

from md_equationsLexer import md_equationsLexer


def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    output_path = argv[2]
    

    with open(output_path, 'w', encoding='utf-8') as out:
        # Listener Lexer
        lexer = md_equationsLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(LexerError(out))
        token = lexer.nextToken()

        token_stream = CommonTokenStream(lexer)
        # Listener Parser
        # parser = JanderParser(token_stream)
        # parser.removeErrorListeners()
        # parser.addErrorListener(JanderParserError(out))

        while token.type != Token.EOF:
            nome_token = md_equationsLexer.symbolicNames[token.type]
            # Tratamento do print do token no formato adequado
            print(f"<'{token.text}',{nome_token}>", file= out)

            token = lexer.nextToken()

if __name__ == '__main__':
    main(sys.argv)