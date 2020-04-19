"""
09. Typoglycemia

スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）
を与え，その実行結果を確認せよ．
"""


import random
import click


def solve(sentence: str) -> str:
    lst = []
    for word in sentence.split():
        n = len(word)
        if n <= 4:
            lst.append(word)
        else:
            indexs = [0] + random.sample(range(1, n - 1), k=n - 2) + [n - 1]
            new_word = "".join([word[i] for i in indexs])
            lst.append(new_word)
    return " ".join(lst)


@click.command()
@click.option(
    "--s",
    default="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .",
)
def main(s: str):
    print(solve(s))


if __name__ == "__main__":
    main()
