#include <omp.h>
#include <stdio.h>

int main() {
    int a[5], b[5], c[5];

    /* sum a[i] + b[i] = c[i] using parallelism, via OpenMP */
#pragma omp parallel for
    for (int i = 0; i < 5; i++) {
        c[i] = a[i] + b[i];
    }

    printf("%d\n", c[2]);

    return 0;
}
