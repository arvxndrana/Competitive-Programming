# This is clearly dikstraye's algorithm application but i don't know it so we ball

N,M,S,T = input().split()
N = int(N)
M = int(M)
S = int(S)
T = int(T)

A = []
B = []
for _ in range(M):
    a,b = input().split()
    A.append(a)
    B.append(b)

A = [int(a) for a in A]
B = [int(b) for b in B]

D = []
for a,b in zip(A,B):
    D.append((a,b))

def all_possible_combinations(links):
    buffer = []
    path = []
    for l in links:
        if (l[0] == S):
            buffer.append(l)
            path.append(l)

    for m in buffer:
        if (m)
