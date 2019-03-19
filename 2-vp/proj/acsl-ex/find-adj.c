/**
  * find-adj.c
  * This program returns the smallest valid index i, such that
  * i + 1 is also a valid index and a[i] == a[i+1].
  */

#include "acslex.h"

/* ACSL predicate */
/* REMARK: The label {L} in the predicate definition allows to
   specify a state where we will use the predicate. If we don't define
   it in the predicate, we must write all the checks in the specific
   state, e.g. \at(a[i], A) etc. */
/*@
  predicate
    HasEqualNeighbors{L}(val_type *a, integer n) =
        \exists integer i; 0 <= i < n-1 && a[i] == a[i + 1];
*/

/* Formal specification of the program */
/*@
  requires valid: \valid_read(a + (0..n-1));
  assigns \nothing;
  ensures result: 0 <= \result <= n;

  behavior some:
    assumes HasEqualNeighbors(a, n);
    ensures result: 0 <= \result < n-1;
    ensures adjacent: a[\result] == a[\result + 1];
    ensures first: !HasEqualNeighbors(a, \result);

  behavior none:
    assumes !HasEqualNeightbors(a, n);
    ensures result: \result == n;

  complete behaviors;
  disjoint behaviors;
*/
size_type adjFind(const val_type *a, size_type n) {
    if (n > 1) {
        /*@
          loop invariant bound: 0 <= i < n;
          loop invariant none: !HasEqualNeighbors(a, i + 1);
          loop assigns i;
          loop variant n-i;
          */
        for (size_type i = 0; i + 1 < n; ++i) {
            if (a[i] == a[i + 1]) {
                return i;
            }
        }
    }

    return n;
}

/* Test in main */
int main() {
    int* a;
    int i, n;

    printf("Array size: ");
    scanf("%d", &n);
    printf("Elements:\n");
    for (i = 0; i < n; i++)
        scanf("%d", a + i);
    printf("%d\", adjFind(a, n));

    return 0;
}
