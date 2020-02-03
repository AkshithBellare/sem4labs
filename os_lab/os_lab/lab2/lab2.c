#include <stdio.h>


double fcfs(int np,int time[][2]){
    int wt[np],total_wtime=0,total_tat = 0,et[np],tat[np];
    wt[0] = 0;
    et[0] = time[0][0];
    int i;
    for(i=1; i<np; i++){
        et[i] = et[i-1] + time[i][0];
    }
    for(i=1 ;i<np; i++){
        wt[i] = et[i] - time[i][1] - time[i][0];
        total_wtime += wt[i];
    }
    for(i =0;i<np;i++){
        tat[i] = time[i][0] + wt[i];
        total_tat += tat[i];
    }
    double avg_wtime = total_wtime / (float)np;
    double avg_tat = total_tat / (float)np;
    printf("Average waiting time is:  %f\nAverage turnaround time is: %f\n",avg_wtime,avg_tat);
    return avg_wtime;
}

double sjf(int np,int time[][2]){
    int wt[np],tat[np],et[np],total_wt=0,total_tat=0;
    int i =0,j=0,key1,key2;
    wt[0] = 0;
    et[0] = time[0][1] + time[0][0];
    //sorting based on burst time
    for(i=2; i<np;i++){
        key1 = time[i][0];
        key2 = time[i][1];
        j = i -1;
        while(j>=1 && (time[j][0] > key1)){
            time[j+1][0] = time[j][0];
            time[j+1][1] = time[j][1];
            j--;
        }
        time[j+1][0] = key1;
        time[j+1][1] = key2;
    }
    for(i=1;i<np;i++){
        et[i] = et[i-1] + time[i][0]; 
    }
    for(i=1;i<np;i++){
        wt[i] = et[i] - time[i][1] - time[i][0];
        total_wt += wt[i];
    }

    for(i=1; i<np; i++){
        tat[i] = et[i] + time[i][0];
        total_tat += tat[i];
    }

    double avg_wt = total_wt / (float)np;
    double avg_tat = total_tat / (float)np;
     printf("Average waiting time is:  %f\nAverage turnaround time is: %f\n",avg_wt,avg_tat); 
     return avg_wt;
}

int main(){
    int num_of_proc;
    printf("Enter the number of processes:");
    scanf("%d",&num_of_proc);
    int time[num_of_proc][2];
    printf("Enter burst_time and arrival time(burst_time(space)arrival_time')\n");
    for (int i=0; i<num_of_proc; i++){
        printf("process %d:",i);
        scanf("%d",&time[i][0]);
        scanf("%d",&time[i][1]);
    }    
   double fcfs_avg = fcfs(num_of_proc,time);
   double sjf_avg = sjf(num_of_proc,time);
   //double sjf_avg = sjf(num_of_proc,time);
}