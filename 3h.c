#include <stdio.h>

int main(void)
{
	int a[100],n,i;
	//printf("\Enter the number of values");
	scanf("%d",&n);
	//printf("\nEnter the values");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		if(a[i]==i)
		{
			printf("%d\t",i);
		}
	}
	
	return 0;
}
