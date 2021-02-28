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
    left = 0
    right = len(xs) - 1

    def go(left, right):
        mid = (left + right) // 2
        if xs[mid] == 0:
            return mid + 1
        if left == right:
            if xs[mid] > 0:
                return mid
            else:
                return None
        if xs[mid] > 0:
            return go(left, mid - 1)
        if xs[mid] < 0:
            return go(mid + 1, right)

    if len(xs) == 0:
        return None
    if xs[0] > 0:
        return 0
    else:
        return go(left, right)


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
    def low_index(left, right):

        if left < right:
            if xs[left] == x:
                return left

            mid = (left + right) // 2
            if xs[mid] > x:
                left = mid + 1
            if xs[mid] <= x:
                right = mid
        else:
            if xs[left] == x:
                return left
            else:
                return -1

        return low_index(left, right)

    def high_index(left, right):

        if left < right:
            if xs[right] == x:
                return right

            mid = (left + right) // 2
            if xs[mid] < x:
                right = mid - 1
            elif xs[mid] >= x and left != mid:
                left = mid + 1
            else:
                if xs[left] == x:
                    return left
                else:
                    return -1
        else:
            if xs[right] == x:
                return right
            else:
                return -1

        return high_index(left, right)

    if xs:
        low = low_index(0, len(xs) - 1)
        high = high_index(0, len(xs) - 1)

        if high != -1:
            return high - low + 1
        else:
            return 0
    else:
        return 0


def argmin(f, lo, hi, epsilon=1e-3):

    left = lo
    right = hi

    def go(left, right):
        m1 = left + (right - left) / 4
        m2 = left + (right - left) / 2

        if right - left < epsilon:
            return right
        if f(m1) < f(m2):
            return go(left, m2)
        if f(m1) > f(m2):
            return go(m1, right)

    return go(left, right)
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

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    '''
    def search(lo, hi):

        if hi - lo < epsilon:
            return hi

        m1 = lo + (hi-lo)/4
        m2 = hi - (hi-lo)/2

        if f(m1) < f(m2):
            return search(lo, m2)
        if f(m1) > f(m2):
            return search(m1, hi)

    return search(lo, hi)
    '''
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
