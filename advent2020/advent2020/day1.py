# --- Day 1: Report Repair ---
from typing import List, Optional, Tuple


# Approximately O(N + logN)
def report_repair_1(xs: List[int]) -> Optional[int]:
    """
    Simply calls through to find_pair_that_equals to find the closest sum to
    the target. If its equal it is returned, else None is returned
    """
    TARGET = 2020
    xs.sort()
    (s, a, b) = find_pair_with_sum_closest_to(xs, 0, len(xs) - 1, TARGET)
    if s == TARGET:
        return a * b
    else:
        return None


# Approximately O(N^2 + logN)
def report_repair_2(xs: List[int]) -> Optional[int]:
    """
    Runs a similar algorithm for three elements. First the array is sorted, then
    The lower element xs[i] begins at element 0 and sweeps up (O(N)), we call
    find_pair_with_sum_closest_to on the rest of the upper part of the array (O(N)).
    """
    TARGET = 2020
    xs.sort()
    i = 0
    while i < len(xs) - 1:
        a = xs[i]
        remainder = TARGET - a
        (s, b, c) = find_pair_with_sum_closest_to(xs, i + 1, len(xs) - 1, remainder)

        if s == remainder:
            assert a + b + c == TARGET
            return a * b * c
        else:
            i = i + 1

    return None


# Aproximately O(N)
def find_pair_with_sum_closest_to(
    xs: List[int], start: int, end: int, target: int
) -> Tuple[int, int, int]:
    """
    Given an array, start and end indices, return the sum s and two elements
    xi and xj such that xi + xj are closest in abosulte difference to the
    target. start must be less than than end.
    """
    assert start < end
    i = start
    j = end
    while i != j:
        xi = xs[i]
        xj = xs[j]
        s = xi + xj
        if s == target:
            return s, xi, xj
        elif s < target:
            i = i + 1
        else:
            j = j - 1

    return s, xi, xj


def main():
    with open("data/day1/input.txt") as f:
        lines = f.readlines()
        expenses = list(map(int, lines))

    print(f"Part 1: {report_repair_1(expenses)}")
    print(f"Part 2: {report_repair_2(expenses)}")


if __name__ == "__main__":
    main()
