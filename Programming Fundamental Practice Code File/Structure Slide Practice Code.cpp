#include<stdio.h>
#include<string.h>
struct student{
	char name[50];
	int id;
}s1,s2;

int main(){
	//struct student s1, s2;
	
	strcpy(s1.name,"Ali");
	s2.id=178392;
	
	printf("\n Name of S1 is : %s", s1.name);
	printf("\n ID of S1 is : %d", s2.id);
	
	return 0;
	}
