from pycparser import parse_file

def parse_file_func():
    ast = parse_file(filename = 'fly_by_wire')#'log.c')
    ast.show()
    #print ("I am called")

def show_func_calls():
    fopen = open("log.c", 'w')
    for line in open("papabeach2.c"):
        li=line.strip()
        if not ( li.startswith("/*") or li.startswith("*") or li.startswith("#")):
           if  li.find('//') != -1:
               fopen.write(li.split('//')[0])
               fopen.write("\n")
           elif li.find('uint8_t') != -1:
               fopen.write(line.rstrip().replace("uint8_t", "int"))
               fopen.write("\n")
           elif li.find('uint16_t') != -1:
               fopen.write(line.rstrip().replace("uint16_t", "int"))
               fopen.write("\n")
           elif li.find('bool_t') != -1:
               fopen.write(line.rstrip().replace("bool_t", "int"))
               fopen.write("\n")
           elif li.find('pprz_t') != -1:
               fopen.write(line.rstrip().replace("pprz_t", "int"))
               fopen.write("\n")
           else:
               fopen.write(line.rstrip())
               fopen.write("\n")
    fopen.close()
    parse_file_func()
    
if __name__ == "__main__":
   show_func_calls()
