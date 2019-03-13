// program to test whether max works
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

method Testing() {
    var m := Max(2, 3);
    // must be true or false
    assert m == 3;
}
