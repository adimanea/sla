// function to return max
function max(a : int, b : int) : int {
      if a >= b then a else b
}

method maxTest() { 
      assert max(2, 3) == 3;
}
