#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>

sem_t mutex,writeblock; //creating reader and write semaphores
int data = 0,rcount = 0; 

void *reader(void *arg)
{
  int f;
  f = ((int)arg); 
  sem_wait(&mutex); //locking the mutex for incrementing rcount
  rcount++;
  if(rcount==1) 
   sem_wait(&writeblock); //this is done to not allow the writer to be able to write
  sem_post(&mutex); //releasing the mutex that was locked when incrementing rcount
  printf("Data read by the reader%d is %d\n",f,data);
  sleep(1);
  sem_wait(&mutex); //after finishing reading the mutex is locked again to decrement rcount
  rcount --;
  if(rcount==0)
   sem_post(&writeblock);
  sem_post(&mutex);
}

void *writer(void *arg)
{
  int f;
  f = ((int) arg);
  sem_wait(&writeblock);
  data++;
  printf("Data writen by the writer%d is %d\n",f,data);
  sleep(1);
  sem_post(&writeblock);
}

int main()
{
  int i,b; 
  pthread_t rtid[5],wtid[5];
  sem_init(&mutex,0,1);
  sem_init(&writeblock,0,1);
  for(i=0;i<=2;i++)
  {
    pthread_create(&wtid[i],NULL,writer,(void *)i);
    pthread_create(&rtid[i],NULL,reader,(void *)i);
  }
  for(i=0;i<=2;i++)
  {
    pthread_join(wtid[i],NULL);
    pthread_join(rtid[i],NULL);
  }
  return 0;
}