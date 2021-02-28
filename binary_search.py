#!/bin/python3
'''
JOKE: There are 2 hard problems in computer
science: cache invalidation, naming things, and off-by-1 errors.

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''

    if len(xs) == 0:
        return None

    if len(xs) == 1:
        for x in xs:
            if x < 0:
                return None

    def go(left, right):
        if left == right:
            for i in range(len(xs)):
                if xs[left] == 0:
                    return xs[i]
                if None:
                    return True
                else:
                    return False

        for i, x in enumerate(xs):
            if x > 0:
                return i
            if x < 0:
                left = i + 1
            if x == 0:
                left = i + 1

    return go(0, len(xs) - 1)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    if len(xs) == 0:
        return 0
    if len(xs) == 1 and x in xs:
        return 1
    if xs[0] == x and xs[1] == x:
        return len(xs)

    def lowest_index(xs, x):
        for i, number in enumerate(xs):
            if number == x:
                return i

    def highest_index(xs, x):
        for i, number in enumerate(xs):
            if xs[len(xs) - 1] == x:
                return len(xs)
            if number < x:
                return i

    lowest = lowest_index(xs, x)
    highest = highest_index(xs, x)

    if lowest is None or highest is None:
        return 0
    else:
        return highest - lowest


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that
    takes a float as input and returns a float
    with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of
    the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that
            are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi)
            must be the smallest;
               depending on which one is the smallest,
               you recursively call your function on the
               interval [lo,m2] or [m1,hi]

    APPLICATION:
    Essentially all data mining algorithms
    are just this argmin implementation in disguise.
    If you go on to take the data mining class (CS145/MATH166),
    we will spend a lot of time talking about
    different f functions that can be minimized
    and their applications.
    But the actual minimization code will all
    be a variant of this binary search.

    WARNING:
    The doctests below are not intended to
    pass on your code,
    and are only given so that you have an
    example of what the output should look like.
    Your output numbers are likely to be slightly
    different due to minor implementation details.
    Writing tests for code that uses floating
    point numbers is notoriously difficult.
    See the pytests for correct examples.

    >>> argmin(lambda x: (x - 5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x - 5)**2, -20, 0)
    -0.00016935087808430278
    '''
    def go(lo,hi):
        m1 = lo + (hi-lo)/3
        m2 = lo + ((hi-lo)/3)*2
        #print('lo=',lo,'hi=',hi,'m2=',m2,'m1=',m1)
        if abs(lo-hi) < epsilon:
            return (hi+lo)/2
        if f(m2) < f(m1):
            lo = m1
        if f(m2) > f(m1):
            hi = m2
        if f(m2) == f(m1):
            lo = m1
            hi = m2
        return go(lo,hi)
    return go(lo,hi)

#########################################
#######################################
# the functions below are extra credit
########################################
########################################


def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the
    minimum is guaranteed to be between lo and hi.
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it
    internally uses the find_boundaries function so that
    '''
