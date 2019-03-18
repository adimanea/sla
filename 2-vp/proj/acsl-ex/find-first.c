/**
  * find-first.c
  * This program sequentially searches an array for an element from
  * another array. It returns the first position where it finds any
  * of the elements of the second array.
  *** Requires: func-find.c ***
  */

#include "acslex.h"

/* Reuse find() from find.c */

size_type find(const val_type* a, size_type n, val_type val) {
    /*@
      loop invariant 0 <= i <= n;
      loop invariant \forall integer k; 0 <= k < i ==> a[k] != val;
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

/* ACSL verification */

/*@
  predicate
    HasValue{A}(val_type* a, integer m, integer n, val_type v) =
        \exists integer i; m <= i < n && a[i] == v;
  predicate
    HasValue{A}(val_type* a, integer n, val_type v) =
        HasValue(a, 0, n, v);
  predicate
    HasValueOf{A} (val_type* a, integer m, val_type* b, integer n) =
        \exists integer i; 0 <= i < m && HasValue{A}(b, n, a[i]);
*/

/* Formal specification */
/*@
  requires valid: \valid_read(a + (0..m-1));
  requires valid: \valid_read(b + (0..n-1));

  assigns \nothing;

  ensures result: 0 <= \result <= m;

  behavior found:
    assumes HasValueOf(a, m, b, n);
    ensures bound: 0 <= result < m;
    ensures result: HasValue(b, n, a[\result]);
    ensures first: !HasValueOf(a, \result, b, n);

  behavior not_found:
    assumes !HasValueOf(a, m, b, n);
    ensures result: \result == m;

  complete behaviors;
  disjoint behaviors;
*/

size_type findFirst(const val_type* a, size_type m,
                    const val_type* b, size_type n) {
    /*@
      loop invariant bound: 0 <= i <= m;
      loop invariant not_found: !HasValueOf(a, i, b, n);
      loop assigns i;
      loop variant m-i;
      */

    for (size_type i = 0; i < m; i++) {
        if (find(b, n, a[i]) < n) {
            return i;
        }
    }
    return m;
}

/* Test in main */
int main() {
    int i, n, m;
    int* a;
    int* b;

    printf("First array size: ");
    scanf("%d", &n);
    a = malloc(n * sizeof(*a));     /* allocate memory for a!! */
    printf("Elements: \n");
    for (i = 0; i < n; i++)
        scanf("%d", a + i);

    printf("Second array size: ");
    scanf("%d", &m);
    b = malloc(n * sizeof(*b));     /* allocate memory for b!! */
    printf("Elements: \n");
    for (i = 0; i < m; i++)
        scanf("%d", b + i);

    printf("%d\n", findFirst(a, n, b, m));

    return 0;
}
