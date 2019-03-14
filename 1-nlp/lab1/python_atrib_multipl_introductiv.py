a, b, c = 1, 2, 3

# TODO1: variabilele rotite cu o poziție -> (2, 3, 1)
print([a, b, c][1:] + [a, b, c][:1])

# TODO2: variabilele în ordine inversă -> (3, 2, 1)
print([a, b, c][::-1])

# TODO3: toate variabilele devin suma valorilor inițiale -> (6, 6, 6)
print([a+b+c, a+b+c, a+b+c])
