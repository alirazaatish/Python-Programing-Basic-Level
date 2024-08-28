 /*****C Program to calculate addition of all elements in an array*****/
 
 #include<stdio.h>
 #include<conio.h>
 int main(){
 	int arr[100], num, i, sum;
 	
 	printf("\n Enter the number of element: ");
 	scanf("%d", &num);
 	
 	printf("\n Enter the Value: ");
 	for(i=0; i<num; i++){
 		scanf("%d", &arr[i]);
	 }
	 
	 sum=0;
	 for(i=0; i<num; i++){
	 	sum+=arr[i];
	 }
	 
	 for(i=0; i<num; i++){
	 printf("\n arr[%d]=%d", i, arr[i]);	
	 }
	 
	 printf("\n Sum Of Array is : %d", sum);
	
 	return 0;
 }
 
 
 /*********C Program to display array elements with addresses***********/
 
 #include<stdio.h>
 #include<conio.h>
 int main(){
 	int marks[5]={55,66,77,88,};
 	
 	printf("\n marks[0], Value=%d, Adderss=%u ", marks[0], &marks[0]);
 	printf("\n marks[1], Value=%d, Adderss=%x ", marks[1], &marks[1]);
 	printf("\n marks[2], Value=%d, Adderss=%p ", marks[2], &marks[2]);
 	
 	return 0;
 }
 
 //******2-Dimensional Array
 
 #include<stdio.h>
 int main(){
 	
 	int i, j;
 	int arr[5][3]={{1,2,3},
	 			   {4,6,7},
				   {8,9,1},
				   {11,12,13},
				   {14,15,16}
				   }
	
	for(i=0; i<5; i++){
		for(j=0; j<3; j++){
			Printf("Enter the element: \n");
		}
	}
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
