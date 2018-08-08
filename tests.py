import binary_search as bs


def test_nominal():
    l = list(range(10))
    for i in range(len(l)):
        assert bs.search(l, i) == i
        assert bs.search(l, i, search_stop=bs.SearchStop.GT) == i + 1


def test_not_found():
    l = list(range(2, 8))
    for search_stop in bs.SearchStop:
        for val in [-1, 0, 1]:
            assert bs.search(l, val, search_stop=search_stop) == 0

        for val in [8, 9]:
            assert bs.search(l, val, search_stop=search_stop) == len(l)


def test_equal_values():
    l = (2, 2, 3, 4)
    assert bs.search(l, 2) == 0
    assert bs.search(l, 2, search_stop=bs.SearchStop.GT) == 2
    assert bs.search(l, 3) == 2
