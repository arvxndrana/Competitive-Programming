# https://atcoder.jp/contests/abc477/tasks/abc477_a

t = ['B', 'Y', 'R']
c = input()

k = t.index(c)
if (t[k] == t[-1]):
    print(t[0])
else:
    print(t[k+1])
