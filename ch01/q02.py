"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

import click


def solve(s1: str, s2: str) -> str:
    lst = []
    for c1, c2 in zip(s1, s2):
        lst.append(c1 + c2)
    return "".join(lst)


@click.command()
@click.option("--s1", default="パトカー")
@click.option("--s2", default="タクシー")
def main(s1: str, s2: str):
    print(solve(s1, s2))


if __name__ == "__main__":
    main()
