/* Exercise 4.17 from "Dinosaur" Essentials */
#include <pthread.h>
#include <stdio.h>
#include <unistd.h> /* for fork() */
#include <wait.h>  /* for wait() */

int value = 0;
void *runner(void *param);      /* the thread */

int main(int argc, char *argv[]) {
    pid_t pid;
    pthread_t tid;
    pthread_attr_t attr;

    pid = fork();

    if (pid == 0) { /* child process */
        pthread_attr_init(&attr);
        pthread_create(&tid, &attr, runner, NULL);
        pthread_join(tid, NULL);
        printf("CHILD: value = %d\n", value);
    }
    else if (pid > 0) { /* parent process */
        wait(NULL);
        printf("PARENT: value = %d\n", value);
    }
    else  /* pid < 0 => fork() failed */
        fprintf(stderr, "Could not create child process\n");
}

void *runner(void *param) {
    value = 5;
    pthread_exit(0);
}

/**
  * The program prints 5 for the child process (which has access to
  * the runner function) and 0 for the parent process (which only
  * has access to the global value = 0).
  */
