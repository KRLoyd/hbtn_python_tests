# Test list with only ints
max_integer([1, 2, 3, 4])

# Test list with not an int
max_integer([a, 1, 2, 4])

# floats
max_integer([4, 4.4, 4.8])

# Large Int
max_integer([99999999999999999999999, 1])

# Test no input
max_integer()

# Test empty list
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

# Test a list of negatives
max_integer([-4, -3, 1, -9])

# Test a list incl None
max_integer([1, 3, None, 7])

# Test None
max_integer(None)

# Test None as list
max_integer([None])

# Test a negative sign in front of list
max_integer(-[1, 4, 5, 6])

# Test a list of floats
max_integer([4.5, 6.7, 7.8])

# Test None None None
max_integer([None, None, None])

# a set
max_integer({5, 8, 0, 99})

# list of sets
max_integer([{5, 7}, {5, 1, 99}])

# list of tuples
max_integer([(1, 1), (99, 99)])

# a tuple
max_integer((1, 99, 5, 8))
