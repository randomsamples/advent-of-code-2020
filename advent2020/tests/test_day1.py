import advent2020.day1 as d


def test_day1():
    expenses = [1721, 979, 366, 299, 675, 1456]
    actual = d.report_repair(expenses)
    assert actual == 30
