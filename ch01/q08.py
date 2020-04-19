"""
08. 暗号文

与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ
"""
import click


def cipher(s: str) -> str:
    def _cipher(s: str) -> str:
        if 97 <= ord(s) <= 128:
            return chr(219 - ord(s))
        else:
            return s

    lst = [_cipher(c) for c in s]
    return "".join(lst)


@click.command()
@click.option("--s", default="AaBbCcDdあいうえお")
def main(s: str):
    ret = cipher(s)
    print(ret)
    print(cipher(ret))


if __name__ == "__main__":
    main()
