#include<stdio.h>
int main()
{
	int n;
	printf("Enter the color : ");
	scanf("%c",&n);

	switch(n)
	{
	case'V':
	case'v':
			printf("It is rainbow color : ");
			break;
	case'I':
	case'i':
			printf("It is rainbow color : ");
			break;
	case'B':
	case'b':
			printf("It is rainbow color : ");
			break;
	case'G':
	case'g':
			printf("It is rainbow color : ");
			break;
	case'Y':
	case'y':
			printf("It is rainbow color : ");
			break;
	case'O':
	case'o':
			printf("It is rainbow color : ");
			break;
	case'R':
	case'r':
			printf("It is rainbow color : ");
			break;
	default:
			printf("It is not rainbow color : ");

	}
	return 0;
}