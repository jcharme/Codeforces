import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    out = []

    # read n num of time in seconds to each bar
    time_to_eat = [int(next(it)) for _ in range(n)]

    # ... solve, append results to out ...
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
