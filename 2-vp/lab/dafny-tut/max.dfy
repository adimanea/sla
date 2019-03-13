// method that computes max
method Max(a: int, b: int) returns (c: int)
    ensures c == a || c == b
    ensures c >= a && c >= b 
{
    if (a > b) {
        return a;
    }
    else {
        return b;
    }
}
