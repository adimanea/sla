// put y = x + 1 and keep the postconditions
// what are the preconditions?
method Abs(x: real) returns (y: real)
    requires x == -0.5;
    ensures 0.0 <= y
    ensures 0.0 <= x ==> x == y
    ensures x < 0.0 ==> y == -x
{
    y := x + 1.0;
}

