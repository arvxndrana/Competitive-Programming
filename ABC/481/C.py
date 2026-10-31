# why is this slowwwwwwwwwww
Q = input()
Q = int(Q)

s = []
for _ in range(Q):
    q = input()
    s.append(q)

u = []
for n in s:
    if (n not in u):
        u.append(n)
    print(u.index(n)+1)
