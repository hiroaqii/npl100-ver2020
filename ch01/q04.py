"""
04. 元素記号

“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ
"""

import click


def solve(s: str):
    a = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    m = {}
    for i, x in enumerate(s.split(), 1):
        if a.count(i) > 0:
            key = x[0]
        else:
            key = x[:2]

        m[key] = i
    return m


@click.command()
@click.option(
    "--s",
    default="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.",
)
def main(s: str):
    print(solve(s))


if __name__ == "__main__":
    main()
