N, K = input().split()
N = int(N)
K = int(K)

A = input().split()
A = [int(n) for n in A]

A_sorted = sorted(A)

i = 0
while (A[i] == A_sorted[i]):
    i += 1

# AGAIN
j = len(A) - 1
while (A[j] == A_sorted[j]):
    j -= 1

distance = abs(j - i + 1)

if (distance <= K):
    print("Yes")
else:
    print("No")
