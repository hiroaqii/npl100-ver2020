"""
05. n-gram

与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ
"""
import click
from typing import List, Union


def n_gram(s: str, n: int) -> Union[List[str], List[List[str]]]:
    return [s[i : i + n] for i in range(len(s) - n + 1)]


@click.command()
@click.option("--i", default=2)
@click.option("--s", default="I am an NLPer")
def main(s: str, i: int):
    print("単語bi-gram：", n_gram(s.split(), i))
    print("文字bi-gram：", n_gram(s, i))


if __name__ == "__main__":
    main()
