"""
14. 先頭からN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ
"""

import click
import pandas as pd


def head(input: str, n: int) -> pd.DataFrame:
    df = pd.read_csv(input, header=None)
    return df.head(n)


@click.command()
@click.option("--input", default="popular-names.txt")
@click.option("--n", default=5)
def main(input: str, n: int):
    df = head(input, n)
    lst = [lst[0] for lst in df.values.tolist()]
    print("\n".join(lst))


if __name__ == "__main__":
    main()
