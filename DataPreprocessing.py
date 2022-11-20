import jieba
import re


def getData(data_set='data4.txt'):
    fileDict = {'data1.txt': '十八大', 'data2.txt': '十九大', 'data3.txt': '二十大', 'data4.txt': '十八大至二十大'}
    # 导入文件数据
    data_set
    with open(data_set, 'r', encoding='UTF-8') as novelFile:
        novel = novelFile.read()
    novelList = re.split(r'([。？！；\n\u3000])', novel)
    # 导入停词
    stopwords = [line.strip() for line in open('stop.txt', 'r', encoding='UTF-8').readlines()]
    # 对文件数据进行分句，并对结果进行清洗
    temp = []
    for nov in novelList:
        if nov != '\n' and nov != '\u3000' and nov not in stopwords:
            temp.append(nov)
    novelList = temp
    # print(novelList)
    temp = []

    # 对分句进行分词处理，并对结果进行清洗
    wordList = list(jieba.lcut(novel))
    for i in wordList:
        if i not in stopwords and i != '\n' and i != '\u3000':
            temp.append(i)
    wordList = temp

    # 统计词频
    # print('词汇总数：%d' % len(wordList))
    wordDict = {}
    # 统计出词频字典
    for word in wordList:
        if word not in stopwords:
            # 不统计字数为一的词
            if len(word) == 1:
                continue
            else:
                wordDict[word] = wordDict.get(word, 0) + 1

    # 对词频进行排序
    wordListSorted = list(wordDict.items())
    wordListSorted.sort(key=lambda e: e[1], reverse=True)

    # 打印前10词频以及柱状图
    topWordNum = 0
    # for topWordTup in wordListSorted[:10]:
    #     print(topWordTup)

    from matplotlib import pyplot as plt

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    x = [c for c, v in wordListSorted]
    y = [v for c, v in wordListSorted]
    plt.bar(x[:10], y[:10])
    plt.title(fileDict[data_set] + "词频分析")
    # 设置x轴标签名
    plt.xlabel("关键词")
    # 设置y轴标签名
    plt.ylabel("词频")
    plt.show()

    # 构建thing列表
    table = []
    for j in novelList:
        thing = []
        for i in range(10):
            if x[i] in j:
                thing.append(x[i])
        table.append(thing)
    return wordListSorted[:10], table
