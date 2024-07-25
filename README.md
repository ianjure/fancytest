## What is Fancytest?
Fancytest offers a [decorator](https://www.geeksforgeeks.org/decorators-in-python/) that will test function call instances in your program.
It will show a simple status of the failed and successful instances.

## How to use Fancytest?
```python
from fancytest import ftest # <-- IMPORT THE PACKAGE

@ftest # <-- ADD THE DECORATOR TO THE FUNCTION YOU WANT TO TEST (@ftest)
def add(a, b):
    return a + b

@ftest # <-- ADD THE DECORATOR TO THE FUNCTION YOU WANT TO TEST (@ftest)
def squared(a):
    return a * a

# FAIL
f = add(2, "b")
squared(f)

# SUCCESS
s = add(1,2)
squared(s)
```

Fancytest will output all instances with their parameters and status.
```
INSTANCE: add(2, 'b') : FAILED
ERROR: unsupported operand type(s) for +: 'int' and 'str'

INSTANCE: squared(None) : FAILED
ERROR: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

INSTANCE: add(1, 2) : SUCCESS
TIME: 0.000ms

INSTANCE: squared(3) : SUCCESS
TIME: 0.000ms
```

