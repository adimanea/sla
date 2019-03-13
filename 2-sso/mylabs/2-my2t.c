/*
 * This program uses 2 threads to increment a global variable.
 * COMPILE WITH
 * cc -pthread my2t.c -o my2t
 * -pthread = to process threads (call POSIX Pthread)
 */
#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>

int a = 0; /* global variable */

void* incrementF(void *arg) {
    /* function to increment a 1 million times */
    for (int i = 0; i < 1000000; i++)
        a++;
}

int main() {
    int i;
    /* create 2 threads */
    pthread_t threads[2];

    for (i = 0; i < 2; i++)
        /* call the increment function on each thread */
        pthread_create(&threads[i], NULL, incrementF, NULL);

    for (i = 0; i < 2; i++)
        /* wait for the threads to finish */
        pthread_join(threads[i], NULL);

    printf("a = %d.\n", a);

    return 0;
}

/**
  * The value returned is not 2 000 000, because the 2 threads SHOULD work
  * in parallel, but there will be intersections. 
  */
