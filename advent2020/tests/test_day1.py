from advent2020.day1 import report_repair_1
from advent2020.day1 import report_repair_2


def test_day1_1():
    expenses = [1721, 979, 366, 299, 675, 1456]
    actual = report_repair_1(expenses)
    assert actual == 514579


def test_day1_2():
    expenses = [1721, 979, 366, 299, 675, 1456]
    actual = report_repair_2(expenses)
    assert actual == 241861950
