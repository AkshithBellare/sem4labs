#include <stdio.h>
#include <unistd.h>

int main(){
    fork();
    if(fork()==0){
        printf("Child process\n");
    }
    else {
        printf("Parent process\n");
    }
}