"""
06. 集合

“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

import click
from q05 import n_gram


def solve(s1: str, s2: str):
    x = set(n_gram(s1, 2))
    y = set(n_gram(s2, 2))
    return {"X": x, "Y": y, "union": x | y, "intersection": x & y, "diff": x - y}


@click.command()
@click.option("--s1", default="paraparaparadise")
@click.option("--s2", default="paragraph")
def main(s1: str, s2: str):
    for k, v in solve(s1, s2).items():
        if k in ("X", "Y"):
            if "se" in v:
                print(k, v, f"({k} に 'se' は含まれる)")
            else:
                print(k, v, f"({k} に 'se' は含まれない)")
        else:
            print(k, v)


if __name__ == "__main__":
    main()
