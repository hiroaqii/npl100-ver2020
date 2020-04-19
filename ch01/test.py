import q00, q01, q02, q03, q04, q05, q06, q07, q08, q09


def test_q00():
    assert q00.solve("stressed") == "desserts"


def test_q01():
    assert q01.solve("パタトクカシーー") == "パトカー"


def test_q02():
    assert q02.solve("パトカー", "タクシー") == "パタトクカシーー"


def test_q03():
    assert q03.solve(
        "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    ) == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


def test_04():
    assert q04.solve(
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    ) == {
        "H": 1,
        "He": 2,
        "Li": 3,
        "Be": 4,
        "B": 5,
        "C": 6,
        "N": 7,
        "O": 8,
        "F": 9,
        "Ne": 10,
        "Na": 11,
        "Mi": 12,
        "Al": 13,
        "Si": 14,
        "P": 15,
        "S": 16,
        "Cl": 17,
        "Ar": 18,
        "K": 19,
        "Ca": 20,
    }


def test_05():
    assert q05.n_gram("I am an NLPer".split(), 2) == [["I", "am"], ["am", "an"], ["an", "NLPer"]]
    assert q05.n_gram("I am an NLPer", 2) == ["I ", " a", "am", "m ", " a", "an", "n ", " N", "NL", "LP", "Pe", "er"]


def test_06():
    ret = q06.solve("paraparaparadise", "paragraph")
    assert ret["union"] == {"pa", "se", "ar", "ag", "ad", "ap", "ph", "ra", "di", "is", "gr"}
    assert ret["intersection"] == {"ar", "pa", "ra", "ap"}
    assert ret["diff"] == {"di", "is", "ad", "se"}


def test_07():
    assert q07.solve("12", "気温", "22.4") == "12時の気温は22.4"


def test_08():
    s = "ABCDEFGabcdefgあ"
    assert q08.cipher(q08.cipher(s)) == s


def test_09():
    s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    ret1 = q09.solve(s)
    ret2 = q09.solve(s)
    lst1 = ret1.split()
    lst2 = ret2.split()
    assert ret1 != ret2
    assert "couldn’t" != lst1[1] != lst2[1]  # 一緒になることもありえる
    assert "that" == lst1[3] == lst2[3]
