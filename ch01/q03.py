"""
03. 円周率

“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

import re
from typing import List
import click


def solve(s: str) -> List[str]:
    return [len(re.findall("[a-zA-Z]", x)) for x in s.split()]


@click.command()
@click.option(
    "--s",
    default="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.",
)
def main(s: str):
    print(solve(s))


if __name__ == "__main__":
    main()
