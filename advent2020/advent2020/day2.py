from dataclasses import dataclass
from typing import Dict, Tuple, Iterable


@dataclass
class PasswordPolicy:
    required_char: str
    min_count: int
    max_count: int

    def check_password(self, password: str) -> bool:
        count_map = {}  # type: Dict[str, int]
        for c in password:
            if c in count_map:
                count = count_map[c]
                count_map[c] = count + 1
            else:
                count_map[c] = 1

        count = count_map.get(self.required_char, 0)
        return count >= self.min_count and count <= self.max_count

    @classmethod
    def parse(self, string: str) -> "PasswordPolicy":
        """
        Parse a string to produce a PasswordPolicy object.
        Expect string to be in the format "{min_uniques}-{max_repeats}"
        e.g., "2-9" would represent min_uniques=2, max_repeats=9
        """
        policy_id_tokens = string.split(" ")
        if len(policy_id_tokens) != 2:
            raise ValueError(
                "Policy parsing error, expected two tokens split by a space"
            )

        required_char = policy_id_tokens[1]

        tokens = policy_id_tokens[0].split("-")
        if len(tokens) != 2:
            raise ValueError(
                "Range parsing error, expected two tokens separated by a '-'"
            )

        try:
            min_count = int(tokens[0])
        except ValueError as e:
            raise ValueError(f"Unable to parse '{tokens[0]}' as an integer.", e)

        try:
            max_count = int(tokens[1])
        except ValueError as e:
            raise ValueError(f"Unable to parse '{tokens[1]}' as an integer.", e)

        return PasswordPolicy(required_char, min_count, max_count)


def parse_input_row(string: str) -> Tuple[PasswordPolicy, str]:
    tokens = list(map(str.strip, string.split(":")))
    if len(tokens) != 2:
        raise ValueError("Expected two tokens split by a ':'")

    password = tokens[1]
    policy = PasswordPolicy.parse(tokens[0])
    return (policy, password)


def parse_and_check_strings(lines: Iterable[str]) -> int:
    check_us = list(map(parse_input_row, lines))
    results = list(map(lambda e: e[0].check_password(e[1]), check_us))
    valid_count = sum(results)
    return valid_count


def main():
    with open("data/day2/input.txt") as f:
        lines = f.readlines()
        check_us = list(filter(lambda val: val is not None and val != "", lines))

    print(f"Part 1: {parse_and_check_strings(check_us)}")


if __name__ == "__main__":
    main()
