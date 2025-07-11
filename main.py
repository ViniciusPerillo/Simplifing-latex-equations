import sys
from antlr4 import *
from Lexer import LexerError
from Parser import ParserError

from md_equationsLexer import md_equationsLexer
from md_equationsParser import md_equationsParser


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
        parser = md_equationsParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ParserError(out))

        parser.document()


if __name__ == '__main__':
    main(sys.argv)