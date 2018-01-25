

int main()
{
    int pid;
    FILE *fp;
    fp = fopen("test.txt","w");/* ---hi-----*/
    char *buff;
    int fd[2];
    int count = 0 ;
    pipe(fd);
    pid = fork();
    printf("the value of pid is--> %d", pid);

    if(pid == 0)
    {
        printf("in if");
        close(fd[1]);
        ioctl(fd[0], FIONREAD, &count);
        fprintf(fp,"Value of count: %d ",count);
        buff = malloc(count);
        fprintf(fp,"\n TIME before read: %s",__TIME__);
        read(fd[0], buff, count);
        fprintf(fp,"\nbuffer: %s\n TIME after read %s", buff, __TIME__);
        wait(10); 
          
        write(fd[1],"THIS is it",10);        
    }
    else{
        printf("\n in else");
        close(fd[0]);
      
        wait(10); 
          
        write(fd[1],"THIS is it",10);
    }
    fclose(fp);
    return 0;
}
