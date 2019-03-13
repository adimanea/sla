/*
 * This program replicates cat(1) at a very basic level,
 * using system calls.
 */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    /* open using system calls => file descriptor */
    int fd = open("myfile.txt", O_RDONLY);

    /* declare variable where content will be stored */
    char* text = (char*)malloc(4096*sizeof(char));

    /* read content in text IN CHUNKS of 4k */
    int readBytes = 0;
    while ((readBytes = read(fd, text, 4096)) != 0)
        write(1, text, readBytes);

    close(fd);
    free(text);

    return 0;
}
