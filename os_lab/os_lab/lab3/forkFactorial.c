#include <stdio.h>
#include <unistd.h> 
#include <sys/wait.h> 
#include <sys/types.h> 
#include <string.h> 
#include <stdlib.h> 

int factorial(int n){
    if(n == 0 || n == 1){
        return 1;
    }
    else{
        return n * factorial(n-1);
    }
}

int main(){
    pid_t pid;
    int n;
    int res = 1;
    printf("Enter the number:");
    scanf("%d",&n);
    if(n < 0){
        printf("Enter a positive number\n");
        exit(0);
    }
    if(pid < 0){
        exit(0);
    }
    int n1 = n/2;
    int n2 = n - n1;
    if(pid==0){
        printf("IN child");
       res = res * factorial(n1);
        printf("child result is %d",res);

    }
    else if(pid > 0){
       res = res * factorial(n2);
    printf(" parent result is %d",res);
    pid = wait(NULL);

    }
}
