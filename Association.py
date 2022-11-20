import itertools


class AssoRule:
    item1 = []
    item2 = []

    def __init__(self, it1, it2):
        self.item1 = it1
        self.item2 = it2

    def getLift(self, table):
        cnt_item1 = 0
        cnt_item2 = 0
        cnt_item1_2 = 0
        for th in table:
            if set(self.item1).issubset(set(th)) and set(self.item2).issubset(set(th)):
                cnt_item1_2 += 1
            if set(self.item1).issubset(set(th)):
                cnt_item1 += 1
            if set(self.item2).issubset(set(th)):
                cnt_item2 += 1
        if cnt_item1 == 0 or cnt_item2 == 0:
            return 0
        lift = cnt_item1_2 * len(table) / (cnt_item2 * cnt_item1)
        return lift


def getAsso(item):
    lst = []
    for i in range(1, len(item)):
        it = itertools.combinations(item, i)
        for j in it:
            item1 = []
            item2 = []
            for k in j:
                item1.append(k)
            item2 = list(set(item) - set(item1))
            node = AssoRule(item1, item2)
            lst.append(node)
    return lst
