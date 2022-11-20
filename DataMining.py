import DataPreprocessing as dpp
import FPtree as fp
import Association as asc
import itertools

wordTop, table = dpp.getData('data4.txt')
freqList = fp.getFreq(table, 50)
# for item,spt in FreqList:
#     print()
temp = []
rules = []
for item, sup in freqList:
    rule = asc.getAsso(item)
    for  r in rule:
        flag = 0
        for k in rules:
            if r.item2 == k.item2 and r.item1 == k.item1:
                flag = 1
                break
        if flag == 0:
            rules.append(r)
# for i in range(len(rules)):
#     for j in range(len(rules) - 1):
#         if rules[j].getLift(table) < rules[j + 1].getLift(table):
#             t = rules[j]
#             rules[j] = rules[j + 1]
#             rules[j + 1] = t

for i in rules:
    print(i.item1,i.item2,i.getLift(table))


# print(wordTop, table)


