import itertools

N, V = input().split()

N = int(N)
V = int(V)

W = input().split()

W = [int(i) for i in W]

W_i = [i+1 for i in range(N)]

summa = itertools.combinations(W_i, 3)
good_summa = []
for x in summa:
    if sum(x) <= V:
        good_summa.append(x)

best_summa = []
for g in good_summa:
    k = 0
    for i in g:
        k += W[i-1]
    best_summa.append(k)

print(max(best_summa))
