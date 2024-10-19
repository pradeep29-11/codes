#include<stdio.h>
int main()
{
	int num1,num2,ans;
	char ch;

	printf("Enter the first number : ");
	scanf("%d",&num1);

	printf("Enter the second number : ");
	scanf("%d",&num2);

	getchar();

	printf("Which performace you want to do(+,-)");
	scanf("%c",&ch);

	switch(ch)
	{
	case '+':
				ans=num1+num2;
				printf("sum of two number is : %d",ans);
				break;
	case '-':
				ans=num1-num2;
				printf("subtracting of two number :%d ",ans);
				break;
	default:
				printf("invalid performace !!");
				break;
	}
	return 0;
}