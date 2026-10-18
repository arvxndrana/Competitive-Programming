# https://atcoder.jp/contests/abc042/tasks/abc042_b
N,L = input().split()

N = int(N)
L = int(L)

S = []
for _ in range(N):
    s = input()
    S.append(s)

S.sort()

cat = ""
for c in S:
    cat += c
print(cat)
