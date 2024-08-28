//Question 2
#include <stdio.h>
void factors(int num) {
int i;
 printf("The factors of %d are: ", num);
 for (i = 1; i <= num; ++i) {
 if (num % i == 0) {
 printf("%d, ", i);
 } }
 printf("\n");
}
int main() {
 int num;
 printf("Enter a number: ");
 scanf("%d", &num);
 factors(num);
 return 0;
}
