"""
01. 「パタトクカシーー」

「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

import click


def solve(s: str) -> str:
    return s[::2]


@click.command()
@click.option("--s", default="パタトクカシーー")
def main(s: str):
    print(solve(s))


if __name__ == "__main__":
    main()
