# Sum Of Multiples

Given a number, find the sum of all the unique multiples of particular numbers up to
but not including that number.

If we list all the natural numbers below 20 that are multiples of 3 or 5,
we get 3, 5, 6, 9, 10, 12, 15, and 18.

The sum of these multiples is 78.

You can make the following assumptions about the inputs to the
`sum_of_multiples` function:
* All input numbers are non-negative `int`s, i.e. natural numbers
including zero.
* A list of factors must be given, and its elements are unique
and sorted in ascending order.

## Running the tests

To run the tests, run `pytest sum_of_multiples_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest sum_of_multiples_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Source

A variation on Problem 1 at Project Euler [http://projecteuler.net/problem=1](http://projecteuler.net/problem=1)
