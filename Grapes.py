N, M = input().split()

N = int(N)
M = int(M)

n = [0 for _ in range(N)]

i = 0
while (M > 0):
    n[i] += 1
    i += 1
    if (i == N):
        i = 0
    M -= 1

for v in n:
    print(v)
