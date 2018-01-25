import ast
import parser
import copy

from pycparser import parse_file, c_ast

ast = parse_file(filename='testMalloc.c')
##ast.show()
for i in range(0,len(ast.ext)):
    ## Look for a function named 'foo'
    if(type(ast.ext[i]) == c_ast.FuncDef and ast.ext[i].decl.name == 'main'):
        ## Store the list of AST node objects in functionBody
        functionBody    = ast.ext[i].body
        print (ast.ext[i])
        ##functionBody.show()
        ## Create a Decl object for the variable test
        id_obj          = c_ast.ID('test')
        identifier_obj  = c_ast.IdentifierType(['int'])
        typedecl_obj    = c_ast.TypeDecl(id_obj.name,None,identifier_obj)
        decl_obj        = c_ast.Decl(id_obj.name,[],[],[],typedecl_obj,None,None)

        ## Append the object to a list.
        ## Concatenate to a copy of existing list of AST objects     
        lst1 = []
        lst1.append(decl_obj)
        lst2 = []
        lst2 = copy.deepcopy(functionBody.block_items)
        lst3 = []
        lst3 = lst1+lst2

        ## Create a modified AST and print content
        functionBody1 = c_ast.Compound(lst3)
        ##functionBody1.show()

