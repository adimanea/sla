/* This program computes sqrt(number) in a separate process thread,
 * using system calls.
 * COMPILE WITH:
 * cc -pthread -o mysqrtt mysqrtthreads.c
 * -pthread = for processing threads (using POSIX Pthread)
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <pthread.h>
#include <sys/types.h>

void* threadF(void* arg) {
    /* cast arg void to int, then take the value */
    int num = *((int*)arg);
    /* DYNAMICALLY allocate to store in heap => kept between thread forking */
    void* result = malloc(sizeof(double));
    /* cast result to double, then take the value */
    *((double*)result) = sqrt(num);
    
    return result;
}

int main() {
    int num = 100;
    pthread_t mySqrt;

    if (pthread_create(&mySqrt, NULL, threadF, &num) != 0)
        /* couldn't create thread for this function */
        return 1;

    double *res;
    /* wait for thread to finish */
    pthread_join(mySqrt, (void**)&res);

    printf("sqrt %d = %lf\n", num, *res);

    free(res);

    return 0;
}
