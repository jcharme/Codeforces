import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import bisect

# O(n + mlogn) -> O(mlogn)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    out = []

    # read n pile sizes
    pileSizes = [0] + [int(next(it)) for pile in range(n)]

    # 1 indexed prefix sum array
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + pileSizes[i]

    m = int(next(it))

    # O(mlogn)
    for worm in range(m):
        q = int(next(it))
        # find first sum >= q
        pile = bisect.bisect_left(prefix, q, 1)
        out.append(pile)

    # ... solve, append results to out ...
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
