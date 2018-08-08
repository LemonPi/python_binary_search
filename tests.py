import binary_search as bs
import datetime


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


def test_custom_key():
    data = """2018-08-01 15:32:48 703
        2018-08-01 17:07:30 651
        2018-08-01 18:28:48 1178
        2018-08-01 20:03:35 1237
        2018-08-01 21:39:06 1155
        2018-08-01 23:15:28 958
        2018-08-02 00:52:34 699
        2018-08-02 02:29:57 454
        2018-08-02 04:06:49 427
        2018-08-02 05:42:51 508
        2018-08-02 07:18:20 609
        2018-08-02 08:53:31 684
        2018-08-02 10:28:29 722
        2018-08-02 12:03:13 729
        2018-08-02 13:37:43 719"""

    fmt = '%Y-%m-%d %H:%M:%S'
    schedule = []
    for line in data.split('\n'):
        parts = line.split()
        dt = datetime.datetime.strptime(' '.join(parts[:2]), fmt)
        schedule.append((dt, int(parts[2])))

    s1 = (datetime.datetime.strptime("2018-08-01 18:01:01", fmt), 100)
    # compare only the datetime
    assert bs.search(schedule, s1, lambda pair: pair[0]) == 2
