"""
11. タブをスペースに置換

タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

import click


def expand(path: str):
    return "".join([line.replace("\t", " ") for line in open(path).readlines()])


@click.command()
@click.option("--path", default="popular-names.txt")
def main(path: str):
    print(expand(path))


if __name__ == "__main__":
    main()
