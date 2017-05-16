# Test list with only ints
max_integer([1, 2, 3, 4])

# Test list with not an int
max_integer([a, 1, 2, 4])

# Test no input
max_integer()

# Tesxt empty list
max_integer([])

# Test with a string
max_integer(["hi", 1, 2, 3])

# Test with a boolean
max_integer([True, False, 1, 2, 3])

# Test a string in a list
max_integer(["hi!", 1, 2, 3])

# Test a string
max_integer("hi")

# Test an int
max_integer(9)

# Test a float
max_integer(5.6)

# Test a negative
max_integer(-99)
