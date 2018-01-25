
void copyData(char *userId) 
{  
    char  smallBuffer[10]; 
    strcpy(smallBuffer, userId);
    puts(smallBuffer);
 }
  
int main(int argc, char *argv[]) 
{  
 char *userId = "abcdfffffee"; 
 copyData (userId); 
}
