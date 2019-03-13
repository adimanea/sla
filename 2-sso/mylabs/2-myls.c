/*
 * This program mimics ls(1), at a very basic level,
 * using system calls.
 */
#include <sys/types.h>
#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int listDir(char* path) {
    DIR* dir = opendir(path);
    /* check for existence */
    if (dir == NULL)
        return 1;

    char newPath[255];
    struct dirent* file = NULL;
    /* check man readdir for the dirent (directory entries) struct */
    while ((file = readdir(dir)) != NULL) { /* as long as you can read from it */
        printf("%s/\t%s\n", path, file->d_name);
        if (file->d_type == DT_DIR && 
                strcmp(file->d_name, ".") != 0 &&
                strcmp(file->d_name, "..") != 0) {
            /* if it is still a file, but NOT . or .. */ 
            strcpy(newPath, path);  /* advance */
            strcat(newPath, "/");   /* add the / postfix */
            strcat(newPath, file->d_name); /* advance */
            listDir(newPath);       /* continue recursively */
        }
    }
    closedir(dir);
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: myls directory\n");
        return 1;
    }

    return listDir(argv[1]);
}

/* Problem: When given relative path (e.g. ./, ../), it writes one / too many */
