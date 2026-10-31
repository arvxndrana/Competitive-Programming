# https://atcoder.jp/contests/abc042/tasks/arc058_a
import itertools
N,K = input().split()

L = len(N)
N = int(N)
K = int(K)

D = input().split()
D = [int(d) for d in D]
W = [x for x in range(10)]

K = set(W)-set(D)
K = list(K)
K.sort()

P = itertools.combinations_with_replacement(K,L)
Y = []
for t in P:
    n = ''
    for i in t:
        n += str(i)
    Y.append(n)

print(Y)

## FAILED ##
