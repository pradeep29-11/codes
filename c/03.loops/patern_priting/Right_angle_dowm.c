#include<stdio.h>
int main()
{
	int n;

	printf("Enter the number : ");
	scanf("%d",&n);

	for(int i=4;i>=1;i--)
	{
		for(int j=1;j<=i;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}