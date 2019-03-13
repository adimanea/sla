// abs to work only on negative values
method Abs(x : int) returns (y : int)
  requires x <= 0;
  ensures x <= 0 ==> y == -x
  ensures y >= 0
  {  
      return -x;
  }
