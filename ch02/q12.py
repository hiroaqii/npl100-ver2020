"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""
import click
import pandas as pd


def cut(input: str, idx: int) -> pd.Series:
    df = pd.read_csv(input, sep="\t", header=None)
    return df[idx]


@click.command()
@click.option("--input", default="popular-names.txt")
@click.option("--idx", default=1)
def main(input: str, idx: int):
    output = f"col{str(idx)}.txt"
    sr = cut(input, idx)
    sr.to_csv(output, header=False, index=False)


if __name__ == "__main__":
    main()
