N, Q = input().split()

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = s[:int(N)]

for i in range(int(N)):
    for j in range(int(N)-1):
        print(f"? {s[j]} {s[j+1]}")
        ans = input()
        if (ans == ">"):
            f = s[:j]
            b = s[j+2:]
            s = f + s[j+1] + s[j] + b

print(f"! {s}")
