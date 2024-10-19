#include<stdio.h>
int main()
{
	int num;

	printf("Enter the number : ");
	scanf("%d",&num);

	switch(num%2)
	{
	case 0:
		printf("%d number is even ",num);
		break;
	case 1:
		printf("%d number is odd ",num);
		break;
	}
	return 0;
}