# --- Day 1: Report Repair ---

# Approximately O(N + logN)
def report_repair_1(xs):
    """
    Simply calls through to find_pair_that_equals to find the closest sum to
    the target. If its equal it is returned, else None is returned
    """
    TARGET = 2020
    xs.sort
    (s, a, b) = find_pair_with_sum_closest_to(xs, 0, len(xs) - 1, TARGET)
    if s == TARGET:
        return a * b
    else:
        return None


# Approximately O(N^2 + logN)
def report_repair_2(xs):
    """
    Runs a similar algorithm for three elements. The lower element xs[i]
    begins at elemtent 0 as usual, but the upper element xs[j] is given as
    a subcomputation which finds the two elements in an upper range which
    are closest to the value TARGET - xs[i] (the remainder). The upper range
    thus needs at least two elements and begins at element len(xs) - 2.
    This upper range is then usd as a sub array to find the two elements that
    come closest to the remainder. The j index is then adjusted as usual.
    """
    TARGET = 2020
    xs.sort()
    s = None
    for i in range(0, len(xs) - 1):
        for j in range(len(xs) - 2, i, -1):
            a = xs[i]
            remainder = TARGET - a
            (s, b, c) = find_pair_with_sum_closest_to(xs, j, len(xs) - 1, remainder)

            if s == remainder:
                assert a + b + c == TARGET
                return a * b * c
            elif s < TARGET:  # too low, increment i
                break
            else:  # s > TARGET, too high decrement j
                pass

    return None


# Aproximately O(N)
def find_pair_with_sum_closest_to(xs, start, end, target):
    """
    Given an array, start and end indices, return the sum s and two elements
    xi and xj such that xi + xj are closest in abosulte difference to the
    target. Sum may be return as None if not enough elements exist.
    """
    assert start < end
    s = None
    xi = 0
    xj = 0
    for i in range(start, end):
        for j in range(end, start, -1):
            xi = xs[i]
            xj = xs[j]
            s = xi + xj

            if s == target:
                return s, xs[i], xs[j]
            elif s < target:  # too low, increment i
                break
            else:  # s > target, too high decrement j
                pass

    return s, xi, xj


def main():
    with open("data/day1/input.txt") as f:
        lines = f.readlines()
        expenses = list(map(int, lines))

    print(f"Part 1: {report_repair_1(expenses)}")
    print(f"Part 2: {report_repair_2(expenses)}")


if __name__ == "__main__":
    main()
