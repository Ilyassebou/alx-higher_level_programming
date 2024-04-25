#!/usr/bin/python3
""" Finds Peak values """

def find_peak(list_of_integers):
    """Find the peak"""
    if not list_of_integers:
        return None
    peak = binary_search(list_of_integers)
    return list_of_integers[peak]

""" binary search algorithm """

def binary_search(a):
    """Iterative binary search of the peak"""
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (hi - lo) // 2 + lo
        if a[mid] > a[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo
