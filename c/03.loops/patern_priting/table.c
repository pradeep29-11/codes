#include<stdio.h>
int main()
{
	for(int i=1;i<=10;i++)
	{
		for(int j=1;j<=4;j++)
		{
			printf("%63d",i*j);
		}
		printf("\n");
	}
	return 0;
}