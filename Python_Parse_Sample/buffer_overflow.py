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
class Decl(c_ast.NodeVisitor):
      def __init__(self,Idname, bufvalue): 
        self.calledFunc = ''
        self.onId = Idname
        self.target = ''
        self.bufvalue = bufvalue
      def visit_Decl(self, node):
          if node.name == self.onId:
             if len(node.init.value)-2 > int(self.bufvalue) :
                 print (" code not safe : overflow ")
             else:
                 print(" code safe : no overfolw")  
          

class FuncCallVisitor(c_ast.NodeVisitor):   
    def __init__(self,Idname): 
        self.calledFunc = ''
        self.onId = Idname
        self.target = ''
        self.flag = 'not'
        ##print (Idname)
    def visit_FuncCall(self, node):               
          if node.name.name == 'strcpy':                
                if node.args.exprs[0].name == self.onId: 
                   self.target = node.args.exprs[1].name   
                   print ("the other variable is", self.target)                           
                       

class ArrayDecl(c_ast.NodeVisitor):
      def visit_ArrayDecl(self, node):
          if type(node.type) == c_ast.TypeDecl:
             print(node.type.type.names, node.type.declname, node.dim.type, node.dim.value)
             objFuncCall = FuncCallVisitor(node.type.declname)
             objFuncCall.visit(ast)
             print(objFuncCall.target)
             objDecl = Decl(objFuncCall.target, node.dim.value)
             objDecl.visit(ast)
             
      
def show_func_calls(filename): 
    global ast 
    ast= parse_file(filename)

    v = ArrayDecl()
    v.visit(ast)
    ##variableMal = v.lval_str
    ##print ( variableMal )
    ##calledFuncMal = v.FuncCalled


if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        func = sys.argv[2]
    else:
        filename = 'testOverflow_type2.c'
        ##func = 'ptr_one'
  
    show_func_calls(filename)
