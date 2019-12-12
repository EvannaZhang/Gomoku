import sys, getopt
import random
from multiprocessing import Pool    #
import time


class node:
    def __init__(self, num, th, now):
        self.num = num
        self.neighbor = []
        self.value = []
        self.threshold = th
        self.now = now
        self.active = False


def cal(timeout):
    global save, nodeList, iteration

    start = time.time()
    ans_count = 0
    ans_sum = 0
    ite_lt = 0
    while True:
        ite_lt += 1
        ActivitySet = save
        for a in range(1, pointCount + 1):
            nodeList[a - 1].active = False
            nodeList[a - 1].now = 0
        for j in range(len(seeds_context)):
            nodeList[int(seeds_context[j]) - 1].active = True
        for j in range(1, pointCount + 1):
            nodeList[j - 1].threshold = random.random()
        count = len(ActivitySet)
        while len(ActivitySet) > 0:
            newActivityList = []
            for a in ActivitySet: #int
                index = -1
                for n in nodeList[a-1].neighbor: #Int
                    index += 1
                    if nodeList[n-1].active is False: #inactive
                        nodeList[n - 1].now += nodeList[a-1].value[index]
                        if nodeList[n - 1].now >= nodeList[n - 1].threshold:
                            newActivityList.append(n)
                            nodeList[n-1].active = True

            count += len(newActivityList)
            ActivitySet = newActivityList

        if time.time() - start > timeout - 3:
            print(ite_lt)
            return ans_sum/ans_count

        ans_count += 1
        ans_sum += count

def caic(timeout):
    global save, nodeList, iteration


    start = time.time()
    ans_count = 0
    ans_sum = 0
    ite_ic = 0
    while True:
        ite_ic += 1
        ActivitySet = save
        for a in range(1, pointCount + 1):
            nodeList[a - 1].active = False
        for j in range(len(seeds_context)):
            nodeList[int(seeds_context[j]) - 1].active = True

        count = len(ActivitySet)

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
                            nodeList[n-1].active = True

            count += len(newActivityList)
            ActivitySet = newActivityList

        if time.time() - start > timeout - 3:
            print(ite_ic)
            return ans_sum/ans_count

        ans_count += 1
        ans_sum += count


if __name__ == "__main__":
    start = time.time()
    argv = sys.argv[1:]
    n = ''
    s = ''
    m = ''
    t = ''
    try:
        opts, args = getopt.getopt(argv, "hi:s:m:t:", ["network=", "seeds=", "model=", "time="])
    except getopt.GetoptError:
        print('test.py -i <network> -s <seeds> -m <model> -t <time')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <network> -s <seeds> -m <model> -t <time')
            sys.exit(0)
        elif opt in ("-i", "--network"):
            n = arg
        elif opt in ("-s", "--seeds"):
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
    file_s = open(s)
    seeds_context = file_s.readlines()
    file_n.close()
    file_s.close()
    ans = 0
    time_limit = float(t)   #

    ActivitySet = []
    nodeList = []

    for i in range(1, pointCount + 1):
        tmp = node(i, 0, 0)
        nodeList.append(tmp)

    for i in range(len(seeds_context)):
        ActivitySet.append(int(seeds_context[i]))
        nodeList[int(seeds_context[i]) - 1].active = True

    save = ActivitySet
    for i in range(edgeCount):
        temp = network_context[i+1].split(' ')
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
    total_sum = 0
    total_cnt = 0
    for tmp in result:
        total_sum += tmp
        total_cnt += 1

    print(total_sum / total_cnt)
    print(time.time()-start)
    sys.stdout.flush()
