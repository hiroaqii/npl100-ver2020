import subprocess
import q10, q11


def cmd(lst, split_newlin=False):
    ret = subprocess.run(lst, stdout=subprocess.PIPE).stdout.decode("utf-8")
    print(ret)
    if split_newlin:
        return ret.split("\n")
    else:
        return ret.split()


def test_q10():
    ret = cmd(["wc", "popular-names.txt"])
    assert q10.wc("popular-names.txt") == int(ret[0])


def test_q11():
    ret = cmd(["expand", "-t", "1", "popular-names.txt"], split_newlin=True)
    assert q11.expand("popular-names.txt") == "\n".join(ret)
