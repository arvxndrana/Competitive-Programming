# https://atcoder.jp/contests/abc042/tasks/abc042_a

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

phrases = [A,B,C]
fives = phrases.count(5)
sevens = phrases.count(7)


if (fives == 2 and sevens == 1):
    print("YES")
else:
    print("NO")
