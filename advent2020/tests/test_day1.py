from advent2020.day1 import report_repair_1
from advent2020.day1 import report_repair_2
from assertpy import assert_that


def test_day1_1():
    expenses = [1721, 979, 366, 299, 675, 1456]
    actual = report_repair_1(expenses)
    assert_that(actual).is_equal_to(514579)


def test_day1_2():
    expenses = [1721, 979, 366, 299, 675, 1456]
    actual = report_repair_2(expenses)
    assert_that(actual).is_equal_to(241861950)
