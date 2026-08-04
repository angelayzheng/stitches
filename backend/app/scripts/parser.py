"""
Parser for custom crochet pattern language.
"""

import re


class Parser:

    stitches: dict[str, list]

    def __init__(self, stitches: dict[str, list]) -> None:
        self.stitches = stitches

    def parse_from_file(self, filename: str) -> list[Instruction]:
        """
        Parse instructions from a file.
        """
        with open(filename, "r") as f:
            lines = [line.rstrip("\r\n") for line in f if line.strip()]

        instructions: list[Instruction] = []

        for line in lines:
            # Remove pound symbol for comments and separate by comma
            # Issue: be careful of commas inside of square brackets
            line_split = line.split("#", 1)[0].split(",")

            for i in line_split:
                instructions.append(self.parse_instruction(i))

        return instructions

    def parse_instruction(self, s: str) -> Instruction:
        """
        Parse instructions from a single instruction string. May contain recursion.

        Preconditions:
            - s contains only a top-level instruction
        """
        split = s.split("-")

        assert len(split) > 1

        return Instruction(split[0], {}, int(split[1]))


class Instruction:

    name: str
    args: dict[str, int]
    num: int

    def __init__(self, name: str, args: dict[str, int], num: int) -> None:
        self.name = name
        self.args = args
        self.num = num

    def __str__(self) -> str:

        if not self.args:
            return f"{self.name}-{self.num}"

        return f"{self.name}({self.args})-{self.num}"


if __name__ == "__main__":
    parser = Parser({})

    test = parser.parse_from_file("../data/simple.txt")

    for i in test:
        print(i)
