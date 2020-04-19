"""
10. 行数のカウント

行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import click


def wc(path: str) -> int:
    return len(open(path).readlines())


@click.command()
@click.option("--path", default="popular-names.txt")
def main(path: str):
    print(wc(path))


if __name__ == "__main__":
    main()
