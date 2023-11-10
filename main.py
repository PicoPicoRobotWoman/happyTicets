from collections import defaultdict
from itertools import product

if __name__ == '__main__':

    map = defaultdict(int)

    for n1, n2 in product(range(10), repeat=2):
        map[n1 + n2] += 1

    res = {n1: sum((map[n1 + n2] ** 2) - 1 for n2 in range(10)) for n1 in range(10)}

    for k, v in res.items():
        print(f"рулон {k + 1} имеет: {v} счастливых билетов")
