#include<stdio.h>

#include <stdlib.h>

int main() 
{
    long int arr[100000],q,m,n,no=0,temp; 
    scanf("%d", &q);
     for(m = 0; m< q; m++)
       scanf("%ld",&arr[m]);
	 
	 for (m = 0; m < q-1; m++)      
		for (n = 0; n < q-m-1; m++) 
           if (arr[n] < arr[n+1])
              {	temp =arr[n+1];
			  	arr[n+1]=arr[n];
			  	arr[n]=temp;
			  }
	for(m = 0; m< q; m++)
    	no=(no*10)+arr[m];
    	
    	printf("%ld",no);
}
