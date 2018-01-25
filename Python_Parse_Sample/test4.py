from __future__ import print_function
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast, parse_file
import ast
import parser
import copy



##ast = parse_file(filename='testMalloc.c')

class IfVisitor(c_ast.NodeVisitor):
    def __init__(self):
        pass

    def visit_If(self, node):
        node.show()
        self.generic_visit(node);



def start(filename):
    ast = parse_file(filename, use_cpp=True)
    v = IfVisitor()
    v.visit(ast)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
    else:
        filename = 'testMalloc.c'

    start(filename)
