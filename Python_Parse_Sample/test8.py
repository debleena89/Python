##from __future__ import print_function
import sys
import ast
import pdb
import string
# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])
  
from pycparser import c_parser, c_ast, parse_file
  
  
# A visitor with some state information (the funcname it's
# looking for)
#

class ExpParser(ast.NodeVisitor):

    def generic_visit(self, node):
        for x in ast.iter_child_nodes(node):
            ast.NodeVisitor.generic_visit(self, x)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_BinOp(self, node):
        print type(node.op).__name__ 

    def visit_Name(self, node):
        print node.id

if __name__ == '__main__':
    node = parse_file('testMalloc.c')
    v = ExpParser()
    v.visit(node)
