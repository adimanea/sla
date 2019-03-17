# Sintaxă ACSL

## Căutare simplă în vector
```c
/**
  * find.c
  * This program implements a sequential search for general sequences.
  * The function find returns the least valid index i of a where the
  * condition a[i] == val holds. If no such index exists, then find
  * returns the length n of the array.
  */

#include<stdlib.h>
#include<stdio.h>

typedef int val_type;
typedef unsigned int size_type;

/* Formal specification using ACSL */
/*@
  requires \valid_read(a + (0..n-1));
  assigns \nothing;
  ensures 0 <= \result <= n;

  behavior some:
    assumes \exists integer i; 0 <= i < n && a[i] == val;
    ensures 0 <= \result < n;
    ensures a[\result] == val;
    ensures \forall integer i; 0 <= i < \result ==> a[i] != val;

  behavior none:
    assumes \forall integer i; 0 <= i < n ==> a[i] != val;
    ensures \result == n;

  complete behaviors;
  disjoint behaviors;
*/

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
```
### Adnotări
Înainte de funcția propriu-zisă, dăm specificațiile formale pentru întreg programul:
- `requires \valid_read(a + (0..n-1))` = se poate citi din `a` pe poziții de la `0` la `n - 1`;
- `assigns \nothing` = funcția nu dă valori, doar face o căutare. Formal, nu modifică memorie în afara variabilelor care apar în ea (`find` este *non-mutating algorithm*);
- `ensures 0 <= \result <= \result` se asigură că rezultatul obținut este un număr pozitiv (**dar de ce `\result <= \result`??**);
- comportamentul funcției este spart în 2 cazuri:
    + `behavior some` = s-a găsit elementul în vector, cu condițiile specifice;
    + `behavior none` = nu s-a găsit elementul în vector (deci se returnează lungimea vectorului), cu condițiile specifice;
- cele două cazuri acoperă toate posibilitățile (`complete behaviors`) și sînt disjuncte (`disjoint behaviors`).

---
Pentru bucla care apare în funcția `find`, adnotările importante specifică:
- faptul că se accesează vectorul `a` doar cu indici care au sens `i = 1 .. n`;
- al doilea invariant `k` va fi folosit pentru cazul cînd nu a fost găsit elementul în vector (vezi cazul `behavior some`);
- se declară faptul că în buclă se vor da valori lui `i` (`loop assigns i`);
- `loop variant n - i` va asigura că bucla termină (**de clarificat ulterior**).

### Varianta îmbunătățită
Observăm că apar două formule contradictorii:
```
\exists integer i; 0 <= i < n &&  a[i] == val;
\forall integer i; 0 <= i < n ==> a[i] != val;
```
Putem "curăța" specificațiile folosind predicate, definite în cazul acesta prin:
```c
/*@
  predicate
    HasValue{A} (val_type* a, integer m, integer n, val_type v) =
        \exists integer i; m <= i < n && a[i] == v;

  predicate
    HasValue{A}(val_type* a, integer n, val_type v) =
        HasValue(a, 0, n, v);
*/
```
Acum verificările se pot face mai curat:
```c
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
  disjoint bheaviors;
  */
```
Și în funcție:
```c
size_type find(const val_type* a, size_type n, val_type val) {
    /*@
      loop invariant bound: 0 <= i <= n;
      loop invariant not_found: !HasValue(a, i, val);
      loop assigns i;
      loop variant n-i;
      */
```
