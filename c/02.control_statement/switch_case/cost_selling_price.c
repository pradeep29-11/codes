#include<stdio.h>
int main()
{
	int cost_price,selling_price,ans;

	printf("Enter the cost price of item : ");
	scanf("%d",&cost_price);

	printf("Enter the selling price : ");
	scanf("%d",&selling_price);

	switch(cost_price>selling_price)
	{
	case 1:
			ans=cost_price-selling_price;
			printf("Seller get profit is %d rupes",ans);
			break;

	case 0:
			ans=selling_price-cost_price;
			printf("seller get lose of %d rupes",ans);
			break;
	}
	return 0;
}