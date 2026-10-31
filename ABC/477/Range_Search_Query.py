# https://atcoder.jp/contests/abc477/tasks/abc477_c

Q = input()
Q = int(Q)

S = input()
T = input()

for _ in range(Q):
    b,e = input().split()
    b = int(b) - 1
    e = int(e)

    if (T in S[b:e]):
        print('Yes')
    else:
        print('No')
