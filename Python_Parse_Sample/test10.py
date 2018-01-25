from __future__ import print_function
import sys
  
# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])
  
from pycparser import c_parser, c_ast, parse_file
  
  
# A visitor with some state information (the funcname it's
# looking for)
#
class IDVisitor(c_ast.NodeVisitor):
    def __init__(self, funcname):
        self.funcname = funcname
  
    def visit_ID(self, node):
        if node.name == self.funcname:
            print('%s called at' % (
                    self.funcname))
  
  
def show_func_calls(filename, funcname):
    ast = parse_file(filename, use_cpp=True)
    v = IDVisitor(funcname)
    v.visit(ast)
  
  
if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        func = sys.argv[2]
    else:
        filename = 'testMalloc.c'
        func = 'ptr_one'
  
    show_func_calls(filename, func)
