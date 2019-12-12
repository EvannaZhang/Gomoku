import sys, getopt
import random
from multiprocessing import Pool    #
import time
import numpy as np


class node:
    def __init__(self, num, th, now):
        self.num = num
        self.neighbor = []
        self.value = []
        self.threshold = th
        self.now = now
        self.active = False
        self.influence = 0


def cal(timeout):
    np.random.seed(np.random.randint(0, 10 ** 9))
    global nodeList
    start = time.time()

    for a in range(1, pointCount + 1):
        nodeList[a - 1].active = False
        nodeList[a - 1].now = 0

    seedlist = []
    seedlist_ans = 0
    count_tmp = 0
    biaoji = []
    influence = []
    for i in range(0, pointCount+1):
        biaoji.append(int(0))
        influence.append(int(0))

    while count_tmp < output_count:
        sec = int(pointCount * random.random())
        if 0 < sec < pointCount + 1:
            if biaoji[sec] == 0:
                seedlist.append(sec)
                biaoji[sec] = 1
                count_tmp += 1

    #print(seedlist)

    #ans_count = 0
    #ans_sum = 0
    for t in range(5):
        ActivitySet = seedlist
        for a in range(1, pointCount + 1):
            nodeList[a - 1].active = False
            nodeList[a - 1].now = 0
        for j in range(output_count):
            nodeList[seedlist[j] - 1].active = True
        for j in range(1, pointCount + 1):
            nodeList[j - 1].threshold = random.random()
        #count = len(ActivitySet)
        while len(ActivitySet) > 0:
            newActivityList = []
            for a in ActivitySet: #int
                index = -1
                for n in nodeList[a-1].neighbor: #Int
                    index += 1
                    if nodeList[n - 1].active is False: #inactive
                        nodeList[n - 1].now += nodeList[a-1].value[index]
                        if nodeList[n - 1].now >= nodeList[n - 1].threshold:
                            influence[a-1] += 1
                            newActivityList.append(n)
                            nodeList[n-1].active = True

            #count += len(newActivityList)
            ActivitySet = newActivityList

        #ans_count += 1
        #ans_sum += count

    #seedlist_ans = ans_sum/ans_count

    while True:
        for a in range(1, pointCount + 1):
            nodeList[a - 1].active = False
            nodeList[a - 1].now = 0

        biaoji = []
        for i in range(0, pointCount+1):
            biaoji.append(int(0))

        seedlist_now = []
        seedlist_ans_now = 0
        count_tmp = 0
        while count_tmp < output_count:
            sec = random.random()
            sec *= pointCount
            sec = int(sec)
            if 0 < sec < pointCount + 1:
                if biaoji[sec] == 0:
                    seedlist_now.append(sec)
                    biaoji[sec] = 1
                    count_tmp += 1

        #print(seedlist_now)
        #ans_count = 0
        #ans_sum = 0
        for t in range(5):
            ActivitySet = seedlist_now
            for a in range(1, pointCount + 1):
                nodeList[a - 1].active = False
                nodeList[a - 1].now = 0
            for j in range(output_count):
                nodeList[seedlist_now[j] - 1].active = True
            for j in range(1, pointCount + 1):
                nodeList[j - 1].threshold = random.random()
            #count = len(ActivitySet)
            while len(ActivitySet) > 0:
                newActivityList = []
                for a in ActivitySet:  # int
                    index = -1
                    for n in nodeList[a - 1].neighbor:  # Int
                        index += 1
                        if nodeList[n - 1].active is False:  # inactive
                            nodeList[n - 1].now += nodeList[a - 1].value[index]
                            if nodeList[n - 1].now >= nodeList[n - 1].threshold:
                                influence[a-1] += 1
                                newActivityList.append(n)
                                nodeList[n - 1].active = True

                #count += len(newActivityList)
                ActivitySet = newActivityList

            #ans_count += 1
            #ans_sum += count

            if time.time() - start > timeout - 3:
                return influence

        #if ans_sum/ans_count > seedlist_ans:
           # seedlist = seedlist_now
           # seedlist_ans = seedlist_ans_now


def caic(timeout):
    np.random.seed(np.random.randint(0, 10 ** 9))
    global nodeList
    start = time.time()

    for a in range(1, pointCount + 1):
        nodeList[a - 1].active = False
        nodeList[a - 1].now = 0

    seedlist = []
    seedlist_ans = 0
    biaoji = []
    influence = []
    for i in range(0, pointCount+1):
        biaoji.append(int(0))
        influence.append(int(0))
    count_tmp = 0
    while count_tmp < output_count:
        sec = random.random()
        sec *= pointCount
        sec = int(sec)
        if 0 < sec < pointCount + 1:
            if biaoji[sec] == 0:
                seedlist.append(sec)
                biaoji[sec] = 1
                count_tmp += 1

    #print(seedlist)
    #ans_count = 0
    #ans_sum = 0
    for t in range(5):
        ActivitySet = seedlist
        for a in range(1, pointCount + 1):
            nodeList[a - 1].active = False
        for j in range(len(seedlist)):
            nodeList[seedlist[j] - 1].active = True

        #count = len(ActivitySet)

        while len(ActivitySet) > 0:
            newActivityList = []
            for a in ActivitySet: #int
                index = -1
                for n in nodeList[a-1].neighbor: #Int
                    index += 1
                    if nodeList[n-1].active is False: #inactive
                        ram = random.random()
                        if ram < nodeList[a-1].value[index]:
                            newActivityList.append(n)
                            influence[a-1] += 1
                            nodeList[n-1].active = True

            #count += len(newActivityList)
            ActivitySet = newActivityList

        #if time.time() - start > timeout - 3:
            #return ans_sum/ans_count

        #ans_count += 1
        #ans_sum += count

   # seedlist_ans = ans_sum/ans_count

    while True:
        for a in range(1, pointCount + 1):
            nodeList[a - 1].active = False
            nodeList[a - 1].chosenassed = False
            nodeList[a - 1].now = 0

        seedlist_now = []
        seedlist_ans_now = 0
        count_tmp = 0
        biaoji = []
        for i in range(0, pointCount + 1):
            biaoji.append(int(0))
        while count_tmp < output_count:
            sec = random.random()
            sec *= pointCount
            sec = int(sec)
            if 0 < sec < pointCount + 1:
                if biaoji[sec] == 0:
                    seedlist_now.append(sec)
                    biaoji[sec] = 1
                    count_tmp += 1

        #print(seedlist_now)

        #ans_count = 0
        #ans_sum = 0
        for t in range(5):
            ActivitySet = seedlist_now
            for a in range(1, pointCount + 1):
                nodeList[a - 1].active = False
                nodeList[a - 1].now = 0
            for j in range(output_count):
                nodeList[seedlist_now[j] - 1].active = True
            for j in range(1, pointCount + 1):
                nodeList[j - 1].threshold = random.random()
            #count = len(ActivitySet)
            while len(ActivitySet) > 0:

                newActivityList = []
                for a in ActivitySet:  # int
                    index = -1
                    for n in nodeList[a - 1].neighbor:  # Int
                        index += 1
                        if nodeList[n - 1].active is False:  # inactive
                            ram = random.random()
                            if ram < nodeList[a - 1].value[index]:
                                newActivityList.append(n)
                                influence[a-1] += 1
                                nodeList[n - 1].active = True

                #count += len(newActivityList)
                ActivitySet = newActivityList

            #ans_count += 1
            #ans_sum += count

            if time.time() - start > timeout - 3:
                return influence

        #if ans_sum / ans_count > seedlist_ans:
            #seedlist = seedlist_now
            #seedlist_ans = seedlist_ans_now


if __name__ == "__main__":
    start = time.time()
    argv = sys.argv[1:]
    n = ''
    s = ''
    m = ''
    t = ''
    try:
        opts, args = getopt.getopt(argv, "hi:k:m:t:", ["network=", "seedCount=", "model=", "time="])
    except getopt.GetoptError:
        print('test.py -i <network> -k <seedCount> -m <model> -t <time')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <network> -k <seedCount> -m <model> -t <time')
            sys.exit(0)
        elif opt in ("-i", "--network"):
            n = arg
        elif opt in ("-k", "--seedCount"):
            s = arg
        elif opt in ("-m", "--model"):
            m = arg
        elif opt in ("-t", "--time"):
            t = arg

    file_n = open(n)
    network_context = file_n.readlines()
    temp = network_context[0].split(' ')
    pointCount = int(temp[0])
    edgeCount = int(temp[1])

    output_count = int(s)

    file_n.close()
    ans = 0
    time_limit = float(t)

    nodeList = []

    for i in range(1, pointCount + 1):
        tmp = node(i, 0, 0)
        nodeList.append(tmp)

    for i in range(edgeCount):
        temp = network_context[i + 1].split(' ')
        first = int(temp[0])
        second = int(temp[1])
        f = float(temp[2])
        nodeList[first - 1].neighbor.append(second)
        nodeList[first - 1].value.append(f)

    pool = Pool(8)
    timeout = time_limit - (time.time() - start)

    if m == 'LT':
        result = pool.map(cal, [timeout] * 8)
    elif m == 'IC':
        result = pool.map(caic, [timeout] * 8)

    #max = -111
    #seed_out = []

    for tmplist in result:
        for i in range(0, len(tmplist)-1):
            nodeList[i].influence += tmplist[i]

    #after = sorted(nodeList, key=lambda n: n.influence, reverse=True)
    for i in range(0, output_count):
        node_tmp = max(nodeList, key=lambda n: n.influence)
        print(node_tmp.num)
        #print(node_tmp.num)
        nodeList[node_tmp.num - 1].influence = -1

    #for i in range(output_count):
        #print(after[i].num)

    sys.stdout.flush()
