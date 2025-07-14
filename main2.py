import sys
import os
from antlr4 import *
from io import StringIO

from Lexer import LexerError
from Parser import ParserError
from Converter import ConverterVisitor  

from md_equationsLexer import md_equationsLexer
from md_equationsParser import md_equationsParser

def process_file(input_file, output_file):
    input_stream = FileStream(input_file, encoding="utf-8")

    error_buffer = StringIO()

    lexer = md_equationsLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(LexerError(error_buffer))
    token_stream = CommonTokenStream(lexer)

    parser = md_equationsParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ParserError(error_buffer))

    tree = parser.document()

    with open(output_file, 'w', encoding='utf-8') as out:
        error_msg = error_buffer.getvalue()
        if error_msg:
            out.write(error_msg)
            out.write("Fim da compilacao\n")
        else:
            visitor = ConverterVisitor()
            latex = visitor.visit(tree)
            out.write(latex)

def main(argv):
    if len(argv) < 3:
        print("Uso: python main.py <entrada> <saida>")
        return

    input_path = argv[1]
    output_path = argv[2]

    if os.path.isdir(input_path) and os.path.isdir(output_path):
        # Entrada e saída são pastas: processa todos arquivos .txt da pasta entrada
        for filename in os.listdir(input_path):
            if filename.endswith('.txt'):
                input_file = os.path.join(input_path, filename)
                base_name = os.path.splitext(filename)[0]
                output_file = os.path.join(output_path, f"{base_name}.md")
                print(f"Processando {input_file} -> {output_file}")
                process_file(input_file, output_file)
    elif os.path.isfile(input_path):
        # Entrada é arquivo, saída é arquivo (mesmo se existir pasta de saída, processa apenas 1 arquivo)
        process_file(input_path, output_path)
    else:
        print("Erro: Entrada ou saída inválidas. Informe arquivo ou pasta válidos.")

if __name__ == '__main__':
    main(sys.argv)
