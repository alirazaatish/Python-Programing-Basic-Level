/*#include<stdio.h>
#include<string.h>
int main(){
	char ch1[50]={'j','a','v','a','s','c','r','i','p','t','\0'}; // String Array
	char ch2[50]="javaScript"; // String cont
	
	printf("String of Array : %s", ch1);
	printf("\n Continuous String is : %s", ch2);
	
	return 0;
}


// String input using scanf()
#include<stdio.h>
#include<string.h>
int main(){
	char s[10];
	printf("Enter the String: ");
	scanf("%s", s);
	
	printf("You enter the : %s", s);
	return 0;
}
*/
//String input using gets()
#include<stdio.h> 
#include<string.h> 
int main ()  
{  
    char s[20];  
    printf("Enter the string?");  
    gets(s);//scanf("%[^\n]s",s);  
    printf("You entered %s",s);  
}



