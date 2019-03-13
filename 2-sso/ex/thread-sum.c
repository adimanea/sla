/*
 * This program computes the sum of all numbers from 0 to N,
 * using 2 threads. It is Figure 4.9 in "Dinosaur" Essentials
 */

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>     /* for atoi */

int sum;            /* data shared by the threads */
void *runner(void *param);      /* threads will call this function */

int main(int argc, char *argv[]) {
    pthread_t tid;      /* thread identifier */
    pthread_attr_t attr; /* set of thread attributes */

    if (argc != 2) {
        fprintf(stderr, "usage: a.out <integer value>\n");
        return -1;
    }
    if (atoi(argv[1]) < 0) { /* atoi = string to integer */
        fprintf(stderr, "%d must be >= 0\n", atoi(argv[1]));
        return -1;
    }

    /* get the default attributes */
    pthread_attr_init(&attr);
    /* create the thread */
    pthread_create(&tid, &attr, runner, argv[1]);
    /* wait for the thread to exit */
    pthread_join(tid, NULL);

    printf("sum = %d\n", sum);
    return 0;
}

/* The thread will begin control in this function */
void *runner(void *param) {
    int i, upper = atoi(param);
    sum = 0;

    for (i = 1; i <= upper; i++)
        sum += i;

    pthread_exit(0);
    /* terminate running thread and returns the value 0 = success */
}
