# IMPLEMENT my_sum().
# YOU COULD(AND MAYBE HAVE TO) CHANGE PARAMETERS OF THIS FUNCTION.
def my_sum():
    return


## VERIFICATION CODE ##

# Case #1: two keyword argument
assert my_sum(a=1, b=2) == 3
assert my_sum(b='back', a='front') == 'frontback'
assert my_sum(a=-200.0, b=0.0) == -200.0

# Case #2: one argument
assert my_sum('text') == 'text'
assert my_sum(2 ** 100) == 2 ** 100
assert my_sum(a=-3.21e4) == -3.21e4

# Case #3: multiple arguments
assert my_sum(1, 2, 3) == 6
assert my_sum(1, 2, 3, 4, 5, -1, -2, -3, -4, -5) == 0
assert my_sum(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1) == 1

# Case #4: without any parameters
try:
    my_sum()
    exit(1)          # exit if no error occurred
except Exception:    # catch every exception
    pass             # ...and do nothing

print("All test case passed!")
