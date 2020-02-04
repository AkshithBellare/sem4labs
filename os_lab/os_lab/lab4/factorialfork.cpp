#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>
#include<unistd.h>
#include<bits/stdc++.h>
using namespace std;
int main()
{
 int pfds[2];
 int n,f=1,i,resOfChild;
 pipe(pfds);
 cout<<"Enter the number:";
 cin>>n;

 if(!fork())
 {
  for(i=1;i<=n/2;i++)
   f=f*i;
  write(pfds[1],(char *)&f,sizeof(f));
  close(pfds[1]);
  printf("Child: Exiting\n");
 }
 else
 {
  wait(0);
  printf("Parent: reading from pipe\n");
  read(pfds[0],&resOfChild,sizeof(int));
  for(int i=n/2+1;i<=n;i++)
  	f=f*i;
  long res=resOfChild*f;
  printf("Final answer %ld\n",res);
  close(pfds[0]);
 }
 return 0;
}