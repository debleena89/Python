
int main()
	{
		int *ptr_one, *ptr_two, *ptr_three;

		ptr_one = (int *)malloc(sizeof(int));
                ptr_two = (int *)malloc(sizeof(int));
                ptr_three = (int *)malloc(sizeof(int));

		if (ptr_one == 0)
		{
			printf("ERROR: Out of memory\n");
			return 1;
		}

		*ptr_one = 25;
		printf("%d\n", *ptr_one);

		free(ptr_one);    
                free(ptr_three);
                

                *ptr_one = 35;
		printf("%d,%d\n", *ptr_one, *ptr_three);

		return 0;
	}
