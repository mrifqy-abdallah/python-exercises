# Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for
which,

```text
a**2 + b**2 = c**2
```

and such that,

```text
a < b < c
```

For example,

```text
3**2 + 4**2 = 9 + 16 = 25 = 5**2.
```

Given an input integer N, find all Pythagorean triplets for which `a + b + c = N`.

For example, with N = 1000, there is exactly one Pythagorean triplet for which `a + b + c = 1000`: `{200, 375, 425}`.

*NOTE*:  
The description above mentions mathematical sets, but also that a Pythagorean Triplet {a, b, c} _must_ be ordered such that a < b < c (ascending order). This makes Python's `set` type unsuited to this exercise, since it is an inherently unordered container. Therefore please return a list of lists instead (i.e. `[[a, b, c]]`). You can generate the triplets themselves in whatever order you would like, as the enclosing list's order will be ignored in the tests.

## Running the tests

To run the tests, run `pytest pythagorean_triplet_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest pythagorean_triplet_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Source

Problem 9 at Project Euler [http://projecteuler.net/problem=9](http://projecteuler.net/problem=9)
