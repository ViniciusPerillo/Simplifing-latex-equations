import sys
from antlr4 import *
from io import StringIO

from Lexer import LexerError
from Parser import ParserError
from Converter import ConverterVisitor  

from md_equationsLexer import md_equationsLexer
from md_equationsParser import md_equationsParser


def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    output_path = argv[2]

    # Buffer para capturar erros (sem interferir na escrita LaTeX final)
    error_buffer = StringIO()

    # Lexer
    lexer = md_equationsLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(LexerError(error_buffer))
    token_stream = CommonTokenStream(lexer)

    # Parser
    parser = md_equationsParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ParserError(error_buffer))

    tree = parser.document()

    with open(output_path, 'w', encoding='utf-8') as out:
        error_msg = error_buffer.getvalue()
        if error_msg:
            # Escreve os erros no arquivo de saída
            out.write(error_msg)
            out.write("Fim da compilacao\n")
        else:
            # Executa o conversor se não houver erros
            visitor = ConverterVisitor()
            latex = visitor.visit(tree)
            out.write(latex)

if __name__ == '__main__':
    main(sys.argv)