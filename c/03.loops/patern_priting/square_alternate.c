#include<stdio.h>
int main()
{
	int x;

	printf("Enter the number : ");
	scanf("%d",&x);

	for(int i=1;i<=x;i++)
	{
		for(int j=1;j<=x;j++)
		{
			if(j%2!=0)
			{
				printf("* ");
			}
			else
			{
				printf("# ");
			}
			
		}
		printf("\n");
	}
	return 0;
}