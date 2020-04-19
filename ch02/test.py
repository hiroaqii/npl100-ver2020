import subprocess
import q10


def cmd(lst):
    ret = subprocess.run(lst, stdout=subprocess.PIPE)
    return ret.stdout.decode("utf8").split()


def test_q10():
    ret = cmd(["wc", "popular-names.txt"])
    assert q10.wc("popular-names.txt") == int(ret[0])
