"""
Parser for custom crochet pattern language.
"""


class Parser:

    stitches: dict[str, list]

    def __init__(self, stitches: dict[str, list]) -> None:
        self.stitches = stitches

    def parse_from_file(self, filename: str) -> None:
        pass


class Instruction:

    name: str
    args: dict[str, int]
    num: int

    def __init__(self, name: str, args: dict[str, int], num: int) -> None:
        self.name = name
        self.args = args
        self.num = num

    def __str__(self) -> str:
        return f"{self.name}({self.args})-{self.num}"

    def parse_from_string(self, s: str) -> None:
        pass
