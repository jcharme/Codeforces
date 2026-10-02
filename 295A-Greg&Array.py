import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import bisect

# O(n + mlogn) -> O(mlogn)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))  # length of array
    m = int(next(it))  # operations
    k = int(next(it))  # k queries

    out = []

    # read n integers (initial array)
    a = [0] + [int(next(it)) for pile in range(n)]

    # store ops in list
    ops = [None]
    for op in range(m):
        ops.append((int(next(it)), int(next(it)), int(next(it))))

    cnt = [0] * (m + 2)

    # queries
    for q in range(k):
        x = int(next(it))
        y = int(next(it))

        # populate cnt difference array, record # times op is run
        cnt[x] += 1
        cnt[y + 1] -= 1

    # prefix sum of cnt for freq of each op
    for i in range(1, m + 1):
        cnt[i] += cnt[i - 1]

    add = [0] * (n + 2)
    for i in range(1, m + 1):
        if cnt[i] > 0:
            l, r, d = ops[i]
            add[l] += cnt[i] * d
            add[r + 1] -= cnt[i] * d

    # prefix sum of add for addition values
    for i in range(1, n + 1):
        add[i] += add[i - 1]

    # combine add with original array
    for i in range(1, n + 1):
        out.append(a[i] + add[i])

    # ... solve, append results to out ...
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
