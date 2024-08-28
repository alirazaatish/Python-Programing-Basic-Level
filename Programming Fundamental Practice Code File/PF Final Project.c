#include<stdio.h>
#include <stdlib.h>
#include<string.h>

// Global Variables
int total_Ammount=100;
int deposite_Ammount; 
int withdraw_Ammount;
int transfer_Ammount;

int total_deposite=0;
int total_withdraw=0;
int total_transfer=0;

char input_name[100];
int input_id;
char input_password[50];

// Functions decleration
int menu();
void deposite();
void withdraw();
void transfer();
void checkDetails();
void checkDetails_at_last();

// Data Structure
struct User {
    char name[100]; 
    int id;
    char password[50];
};

int main(){
	 
    struct User user1 = {"Ali Raza", 112233, "ali123"};
    struct User user2 = {"Sohail Abbas", 445566, "sohail123"};
    struct User user3 = {"Aimen Zainab", 778899, "aimen123"};
    
    
    struct User users[] = {user1, user2, user3};
    int num_users = 3;
    
    printf("\n---:KARAKORAM COOPERATIVE BANK LIMITED (KCBL):----\n");
    printf("\n---------------------------------------------------\n");
    printf("USER LOGIN:\n");
    printf("-----------------------------------------------------\n");
    printf("\nEnter your name: ");
    fgets(input_name, sizeof(input_name), stdin);
    input_name[strcspn(input_name, "\n")] = '\0';
    printf("\nEnter your ID: ");
    scanf("%d", &input_id);
    printf("\nEnter your password: ");
    scanf("%49s", input_password);

    // Flag to check if login is successful
    int login_success = 0;
    int i;
    
    for (i = 0; i < num_users; i++) {
        if (strcmp(input_name, users[i].name) == 0 && 
            input_id == users[i].id && 
            strcmp(input_password, users[i].password) == 0) {
            login_success = 1;
            break;
        }
    }

    // Display login result
    if (login_success) {
    	printf("\n----------------------------------------------\n");
        printf("Login successful! Welcome, %s.\n", input_name);
        printf("\n-----------------------------------------------\n");
        
        while(1){
		printf("\n");
		switch(menu())
			{
				case 1:
					deposite();
					total_deposite+=deposite_Ammount;
					break;
				case 2:
					withdraw();
					if(withdraw_Ammount<total_Ammount){
						total_withdraw+=withdraw_Ammount;
					}
					break;
				case 3:
					transfer();
					if(transfer_Ammount<total_Ammount){
						total_transfer+=transfer_Ammount;
					}
					break;
				case 4:
					checkDetails();
					break;
				case 5:
					checkDetails_at_last();
					printf("\nExiting the program. Goodbye!\n");
                    exit(0);
				default:
				    printf("\n Invalid choice!");
			}
	}
    } else {
        printf("Login failed. Please check your credentials and try again.\n");
    }
           
	return(0);
}

int menu()
{
	    int choice;
	 	printf("\nBanking System Menu:\n");
        printf("1. Deposit Ammount\n");
        printf("2. Withdraw Ammount\n");
        printf("3. Transfer Ammount\n");
        printf("4. Check Details\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        return choice;
}

// Functions defination
void deposite()
{
	printf("\nEnter the Ammount you want to deposite: ");
	scanf("%d", &deposite_Ammount);
	total_Ammount+=deposite_Ammount;
}

void withdraw()
{
	printf("\nEnter the Ammount you want to withdraw: ");
	scanf("%d", &withdraw_Ammount);
	if(withdraw_Ammount<total_Ammount){
		total_Ammount+=withdraw_Ammount;
	}
	else{
		printf("\nSorry! Insufficient balance!");
	}
}

void transfer()
{
	printf("\nEnter the Ammount you want to transfer: ");
	scanf("%d", &transfer_Ammount);
	if(transfer_Ammount<total_Ammount){
		total_Ammount-=transfer_Ammount;
	}
	else{
		printf("\nLess Ammount! Transfer is not Possible.");
	}
}

void checkDetails(){
	printf("\n Total Ammount = %d ", total_Ammount);
	printf("\n Total Deposite = %d ", total_deposite);
	printf("\n Total Withdraw = %d", total_withdraw);
	printf("\n Total Transfered Ammount = %d", total_transfer);
}

void checkDetails_at_last(){
	printf("\n\n****************************************************");
	printf("\nYour Name is %s", input_name);
	printf("\nYour ID is %d", input_id);
	printf("\n Total Ammount = %d ", total_Ammount);
	printf("\n Total Deposite = %d ", total_deposite);
	printf("\n Total Withdraw = %d", total_withdraw);
	printf("\n Total Transfered Ammount = %d", total_transfer);
	printf("\n**********Thanks!************");
}
