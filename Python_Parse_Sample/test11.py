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
class AssignmentVisitor(c_ast.NodeVisitor):
     def visit_Assignment(self, node):
         if type(node.lvalue) == c_ast.ID:
                lval_str = node.lvalue.name
         rval_str = node.rvalue
         if type(rval_str) == c_ast.Cast:
            print('%s --> %s' % (
                    lval_str, type(rval_str)))
         else:  
               print ("not match")
  
  
def show_func_calls(filename):
    ast = parse_file(filename, use_cpp=True)
    v = AssignmentVisitor()
    v.visit(ast)
  
  
if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        func = sys.argv[2]
    else:
        filename = 'testMalloc.c'
        ##func = 'ptr_one'
  
    show_func_calls(filename)
