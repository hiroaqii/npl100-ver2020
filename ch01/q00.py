"""
00. 文字列の逆順

文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

import click


def solve(s: str) -> str:
    return s[::-1]


@click.command()
@click.option("--s", default="stressed")
def main(s: str):
    print(solve(s))


if __name__ == "__main__":
    main()
