

from pycparser import parse_file
ast = parse_file(filename='testMalloc.c')
ast.show()


