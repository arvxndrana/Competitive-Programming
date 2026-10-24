# Copied code from TWITCH STREAMER errichto
N,K = input().split()
A = input().split()

N = int(N)
K = int(K)
A = [int(a) for a in A]

answer = 0
for i,a in enumerate(A):
    if (a == K):
        answer += 1
    if (i >= 1):
        prev = A[i-1]
        current = a
        if ((min(prev, current) < K) and (max(prev, current) > K)):
            answer += 1
print(answer)
