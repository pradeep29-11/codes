#include<stdio.h>

int  even_number(int a)
{
	if(a%2==0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
	positive_number(int x)
	{
		if(x>=0)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}

}
int main()
{
	int num,number,A;

	printf("Enter the number : ");
	scanf("%d",&num);

	number=even_number(num);
	if(number==1)
	{
		printf("%d is even number \n ",num);
	}
	else
	{
		printf("%d numberis odd number\n ",num);
	}

	A=positive_number(num);

	if(A==1)
	{
		printf("%d is the positive number\n ",num);
	}
	else
	{
		printf("%d number is negative\n ",num);
	}
	return 0;
}