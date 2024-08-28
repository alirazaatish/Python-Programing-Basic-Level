
#include <stdio.h>

int main() {
    int arr[10] = {11, 22, 33};
    //int arr[10];
    int *p;
    p = &arr;  // No need to use &arr, just use arr

    printf("Address of array: %p\n",  p);

    return 0;  // Return 0 to indicate successful execution
}

#include <stdio.h>

// Function declaration
void greet() {
    printf("Hello, World!\n");
}

int main() {
    // Declare a function pointer
    void (*funcPtr)();

    // Assign the address of the function 'greet' to the function pointer
    funcPtr = &greet;

    // Call the function using the function pointer
    (*funcPtr)();

    // Alternatively, you can call it without dereferencing
    funcPtr();

    // Print the address of the function using the function pointer
    printf("\nAddress of function greet: %p\n", (void*)funcPtr);

    return 0;
}

*/

#include <stdio.h>

// Define a structure
struct Person {
    char name[50];
    int age;
};

int main() {
    // Create an instance of the structure
    struct Person person1 = {"John Doe", 30};

    // Declare a pointer to the structure
    struct Person *p;

    // Assign the address of person1 to the pointer
    p = &person1;

    // Access and print the structure members using the pointer
    printf("Name: %s\n", p->name);
    printf("Age: %d\n", p->age);

    // Modify structure members using the pointer
    p->age = 31;

    // Print the modified structure members
    printf("Updated Age: %d\n", p->age);

    return 0;
}


