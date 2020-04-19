"""
07. テンプレートによる文生成

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
"""
import click


def solve(x: str, y: str, z: str) -> str:
    return f"{x}時の{y}は{z}"


@click.command()
@click.option("--x", default="12")
@click.option("--y", default="気温")
@click.option("--z", default="22.4")
def main(x: str, y: str, z: str):
    print(solve(x, y, z))


if __name__ == "__main__":
    main()
