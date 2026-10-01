import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

# O(n) time, O(n) space


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    out = []

    # read string s
    s = next(it).decode("ascii")

    # read number of queries m
    m = int(next(it))

    # derived array b[i]=1 when s[i]==s[i+1]
    b = [0] * (len(s) + 1)

    # prefix sum array of the derived
    p = [0] * (len(s) + 1)

    # O(n)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            b[i] = 1
        else:
            b[i] = 0
        p[i + 1] = p[i] + b[i]

    # each query O(n)
    # process each query
    for q in range(m):
        l = int(next(it))
        r = int(next(it))

        ans = p[r - 1] - p[l - 1]
        out.append(str(ans))

    # ... solve, append results to out ...
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
