/*
// Example for Function without argument and return value
#include<stdio.h>

void find_squ();

int main(){
	
	printf("Funtion is Calling:\n");
	find_squ();
	
	return 0;
}

void find_squ(){
	int num;
	printf("Enter the number: ");
	scanf("%d", &num);
	int square=num*num;
	printf("\n Square of %d is %d: ", num, square);
}

//Example for Function without argument and with return value
#include<stdio.h>

int find_squ();

int main(){
	
	printf("Funtion is Calling:\n");
	int square= find_squ();
	printf("\n Square of num is %d: ", square);
	return 0;
}

 int find_squ(){
 	int num;
	printf("Enter the number: ");
	scanf("%d", &num);
	return (num*num);
 }
 
 
 //Example for Function with argument and without return value
#include<stdio.h>

int find_squ(int num);

int main(){
	int num;
	printf("Enter the number: ");
	scanf("%d", &num);
	printf("Funtion is Calling:\n");
	find_squ(num);
	
	return 0;
}

 int find_squ(int num){
 	int square=num*num;
	printf("\n Square of %d is %d: ", num,square);
 }
 */
 
 //Example for Function with argument and return value
#include<stdio.h>

int find_squ(int num);

int main(){
	int num;
	printf("Enter the number: ");
	scanf("%d", &num);
	printf("Funtion is Calling:\n");
	int square= find_squ(num);
	printf("\n Square of %d is %d: ", num,square);
	
	return 0;
}

 int find_squ(int num){
 	int square=num*num;
 	return square;
 }
 
 
 
