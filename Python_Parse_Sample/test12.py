import sys
import ast
sys.path.extend(['.', '..'])
CPPPATH = '../utils/cpp.exe' if sys.platform == 'win32' else 'cpp'
from pycparser import c_parser, c_ast, parse_file

class FunctionParameter(c_ast.NodeVisitor):

    def visit_FuncDef(self, node):
        #node.decl.type.args.params
        print "Function name is", node.decl.name, "at", node.decl.coord
        print "    It's parameters name  and type is (are)"
        for params in (node.decl.type.args.params):
            print "        ", params.name, params.type


def func_parameter(filename):
    ast = parse_file(filename, use_cpp=True, cpp_path=CPPPATH, cpp_args=r'-I../utils/fake_libc/include')

    vf = FunctionParameter()
    vf.visit(ast)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'hash.c'
    func_parameter(filename)
