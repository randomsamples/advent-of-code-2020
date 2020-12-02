from advent2020.day1 import report_repair


def test_day1():
    expenses = [1721, 979, 366, 299, 675, 1456]
    actual = report_repair(expenses)
    assert actual == 30
