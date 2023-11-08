
if __name__ == '__main__':

    map = {}

    for n1 in range(0, 10):
        for n2 in range(0, 10):
            if n1 + n2 in map:
                map[n1 + n2] += 1
            else:
                map[n1 + n2] = 1

    res = {}

    for n1 in range(0, 10):
        res[n1] = 0
        for n2 in range(0, 10):
            res[n1] += (map[n1 + n2] ** 2) - 1

    for k in res:
        print(res[k])
