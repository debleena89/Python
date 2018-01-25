
void copyData(char *userId) 
{  
    char  smallBuffer[10] = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}; 
        puts(smallBuffer);
 }
  
int main(int argc, char *argv[]) 
{  
 char *userId = "abcdfffffee"; 
 copyData (userId); 
}
