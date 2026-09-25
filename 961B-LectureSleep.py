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
    theorems_min = [int(next(it)) for _ in range(n)]

    # read Mishka's behaviour at each i minute 0 for sleep
    behaviour = [int(next(it)) for _ in range(n)]

    # O(n)
    baseSum = 0
    gain = [0] * n

    for i in range(n):
        if behaviour[i] == 0:
            gain[i] = theorems_min[i]
        else:
            baseSum += theorems_min[i]

    cur = 0
    best = 0

    # sliding window O(n)
    for r in range(n):
        cur += gain[r]
        # Once the right pointer passes the window size,
        # subtract the element falling out the left side
        if r >= k:
            cur -= gain[r - k]

        # Update best sliding window total
        if cur > best:
            best = cur

    out.append(best + baseSum)

    # ... solve, append results to out ...
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
