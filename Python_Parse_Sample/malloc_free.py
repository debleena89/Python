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
ast = None

class FuncCallVisitor(c_ast.NodeVisitor):   
    def __init__(self,Idname): 
        self.calledFunc = ''
        self.onId = Idname
        self.flag = 'not'
        ##print (Idname)
    def visit_FuncCall(self, node):          
          if node.name.name == 'free' and self.flag == 'not':
                if node.args.exprs[0].name == self.onId: 
                       print (self.onId, "got freed") 
                       self.flag = 'check'                            
                       
                ##if node.args.exprs[0].name != self.onId: 
                  ##     print (self.onId, "not got freed")
               ## self.calledFunc = node.name.name
               ##self.onId = node.args.exprs[0].name          
               ##print('%s called at %s' % (
                 ##   node.name.name, node.args.exprs[0].name))
               ##return node.args.exprs[0].name


class AssignmentVisitor(c_ast.NodeVisitor):
     def __init__(self):
          self.lval_str = ''
          self.rval_str = ''
          self.FuncCalled = ''
     def visit_Assignment(self, node):
         if type(node.lvalue) == c_ast.ID:
              self.lval_str = node.lvalue.name
         self.rval_str = node.rvalue
         if type(self.rval_str) == c_ast.Cast: 
               self.FuncCalled = node.rvalue.expr.name.name 
               ##print('%s --> %s' % (
                 ##   self.lval_str, node.rvalue.expr.name.name ))   
               z = FuncCallVisitor(self.lval_str)
               z.visit(ast)
               if z.flag != 'check':
                   print (self.lval_str,"not get freed")
               
               
               ##return self.lval_str
            ## v = FuncCallVisitor.visit_FuncCall()
  
def show_func_calls(filename): 
    global ast 
    ast= parse_file(filename, use_cpp=True)

    v = AssignmentVisitor()
    v.visit(ast)
    variableMal = v.lval_str
    ##print ( variableMal )
    calledFuncMal = v.FuncCalled

    ##z = FuncCallVisitor()
    ##z.visit(ast)
    ##variableFre = z.onId
    ##print ( variableFre )
    ##calledFuncFre = z.calledFunc 

    ##if variableMal == variableFre and calledFuncMal == 'malloc' and calledFuncFre == 'free' :
     ##   print (variableMal, "is called as maaloc and then freed")
  
  
if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        func = sys.argv[2]
    else:
        filename = 'test_Malloc_Function.c'
        ##func = 'ptr_one'
  
    show_func_calls(filename)
