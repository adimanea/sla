/**
  * find-predicate.c
  * This program implements a sequential search for general sequences.
  * The function find returns the least valid index i of a where the
  * condition a[i] == val holds. If no such index exists, then find
  * returns the length n of the array.
  *** Improved version, using predicates. ***
  */

#include<stdlib.h>
#include<stdio.h>

typedef int val_type;
typedef unsigned int size_type;

/* Define ACSL predicates */
/*@
  predicate
    HasValue{A}(val_type* a, integer m, integer n, val_type v) =
        \exists integer i; m <= i < n && a[i] == v;

  predicate
    HasValue{A}(val_type* a, integer n, val_type v) =
        HasValue(a, 0, n, v);
*/

/* Formal specification using ACSL */
/*@
  requires valid: \valid_read(a + (0..n-1));
  assigns \nothing;
  ensures result: 0 <= \result <= n;

  behavior some:
    assumes HasValue(a, n, val);
    ensures bound: 0 <= \result < n;
    ensures result: a[\result] == val;
    ensures first: !HasValue(a, \result, val);

  behavior none:
    assumes !HasValue(a, n, val);
    ensures result: \result == n;

  complete behaviors;
  disjoint behaviors;
  */

size_type find(const val_type* a, size_type n, val_type val) {
    /*@
      loop invariant bound: 0 <= i <= n;
      loop invariant not_found: !HasValue(a, i, val);
      loop assigns i;
      loop variant n-i;
      */
    for (size_type i = 0; i < n; i++) {
        if (a[i] == val) {
            return i;
        }
    }

    return n;
}

/* Test in main */
int main() {
    int i, n, toFind;
    int* a;

    printf("Array size: ");
    scanf("%d", &n);
    printf("Elements: \n");
    for (i = 0; i < n; i++)
        scanf("%d", a + i);
    printf("To find in the array: ");
    scanf("%d", &toFind);
    printf("%d\n", find(a, n, toFind));

    return 0;
}
