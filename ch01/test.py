import q00, q01, q02, q03


def test_q00():
    assert q00.solve("stressed") == "desserts"


def test_q01():
    assert q01.solve("パタトクカシーー") == "パトカー"


def test_q02():
    assert q02.solve("パトカー", "タクシー") == "パタトクカシーー"


def test_q03():
    assert q03.solve(
        "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.ー"
    ) == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
