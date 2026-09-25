import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

# O(n) time, O(n) space


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    out = []

    # read n num of theorems at ith min
    theorems_min = [0] + [int(next(it)) for i in range(n)]

    # read Mishka's behaviour at each i minute 0 for sleep
    behaviour = [0] + [int(next(it)) for i in range(n)]

    # O(n)
    baseSum = 0
    gain = [0] * n
    for i in range(n):
        if behaviour[i] == 0:
            gain[i] == theorems_min[i]
        baseSum += theorems_min[i]

    cur = 0
    best = 0

    # sliding window O(n)
    for r in range(n):
        cur += gain[r]
        # maintain window of size k
        if cur >= k:
            best = max(best, cur)
            # slide forward by removing left most element
            cur -= gain[r - k + 1]

    out.append(best + baseSum)

    # ... solve, append results to out ...
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
