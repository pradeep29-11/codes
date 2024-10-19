#include<stdio.h>
int main()
{
	char ch;

	printf("Enter the character : ");
	scanf("%c",&ch);

	switch(ch)
	{
	case 'A':
	case 'a':
	case 'E':
	case 'e':
	case 'I':
	case 'i':
	case 'O':
	case 'o':
	case 'U':
	case 'u':
			printf("It is vowel !");
			break;
	default :
			printf("It is not vowel !!");
			break;
	}

	return 0;
}