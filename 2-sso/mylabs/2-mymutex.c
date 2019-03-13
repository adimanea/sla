/*
 * This program uses a mutex to remove conflicting operation
 * of 2 threads that race to operate on a global variable.
 */
#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>

/**
 * MUTEX = mutually exclusive operation of threads
 */

int a = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *incF(void *arg) {
    for (int i = 0; i < 1000000; i++) {
        /* lock the mutex, so the threads don't interfere */
        pthread_mutex_lock(&mutex);
        a++;
        /* unlock the mutex to be further used, if needed */
        pthread_mutex_unlock(&mutex);
    }
}
/**
  * NOTE: The mutex will lock each iteration, so there is no concurrency.
  * Putting the lock/unlock outside the for, locks the thread for the whole
  * iteration. Basically, one increases the whole 1mil times, and the other waits.
  */

int main() {
    pthread_t threads[2];
    /* initialize the mutex with NULL */
    pthread_mutex_init(&mutex, NULL);
    int i;

    for (i = 0; i < 2; i++)
        /* create the 2 threads */
        pthread_create(&threads[i], NULL, incF, NULL);

    for (i = 0; i < 2; i++)
        /* wait for the threads to finish */
        pthread_join(threads[i], NULL);

    printf("a = %d.\n", a);
    /* clear the mutex */
    pthread_mutex_destroy(&mutex);

    return 0;
}
