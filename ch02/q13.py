"""
13. col1.txtとcol2.txtをマージ

12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．

"""
import click
import pandas as pd


def paste(input1: str, input2: str) -> pd.DataFrame:
    df1 = pd.read_csv(input1, header=None)
    df2 = pd.read_csv(input2, header=None)
    df = pd.concat([df1, df2], axis=1)
    return df


@click.command()
@click.option("--input1", default="col0.txt")
@click.option("--input2", default="col1.txt")
def main(input1: str, input2: str):
    df = paste(input1, input2)
    df.to_csv("q13_out.csv", sep="\t", header=None, index=False)


if __name__ == "__main__":
    main()
