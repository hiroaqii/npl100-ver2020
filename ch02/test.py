import subprocess
import q10, q11, q12


def cmd(lst, split_newlin=False):
    ret = subprocess.run(lst, stdout=subprocess.PIPE).stdout.decode("utf-8")
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


def test_q12():
    ret1 = cmd(["cut", "-f", "1", "popular-names.txt"])
    sr1 = q12.cut("popular-names.txt", 0)
    assert ret1 == sr1.to_list()

    ret2 = cmd(["cut", "-f", "2", "popular-names.txt"])
    sr2 = q12.cut("popular-names.txt", 1)
    assert ret2 == sr2.to_list()
