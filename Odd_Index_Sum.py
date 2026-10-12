# https://atcoder.jp/contests/abc479/tasks/abc479_a 

N = input()
N = int(N)

A = input().split()
A = [int(a) for a in A]

i = 0
S = 0
while (i < len(A)):
    if (i % 2 == 0):
        S += A[i]
    i += 1
print(S)
