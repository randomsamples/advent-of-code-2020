import textwrap

from assertpy import assert_that  # type: ignore
from pytest import raises

from advent2020.day2 import PasswordPolicy, parse_input_row, parse_and_check_strings


def test_password_policy_parse():
    obj = PasswordPolicy.parse("3-9 a")
    assert_that(obj.required_char).is_equal_to("a")
    assert_that(obj.min_count).is_equal_to(3)
    assert_that(obj.max_count).is_equal_to(9)

    with raises(ValueError):
        obj = PasswordPolicy.parse("34234 a")

    with raises(ValueError):
        obj = PasswordPolicy.parse("3-4-3 a")

    with raises(ValueError):
        obj = PasswordPolicy.parse("sad-1 a")

    with raises(ValueError):
        obj = PasswordPolicy.parse("43-gjfk c")


def test_parse_row():
    res = parse_input_row("2-9 c: ccccccccc")
    assert_that(len(res)).is_equal_to(2)
    assert_that(res[0]).is_equal_to(PasswordPolicy("c", 2, 9))
    assert_that(res[1]).is_equal_to("ccccccccc")


def test_day2_1():
    # expenses = [1721, 979, 366, 299, 675, 1456]
    # actual = password_check(expenses)
    input = textwrap.dedent(
        """\
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
        """
    )

    clean = list(filter(lambda val: val is not None and val != "", input.splitlines()))
    valid_count = parse_and_check_strings(clean)
    assert_that(valid_count).is_equal_to(2)
