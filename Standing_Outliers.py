# https://atcoder.jp/contests/abc477/tasks/abc477_b
N, D = input().split()

N = int(N)
D = int(D)

X = input().split() 
X = [int(x) for x in X]

people_standing_apart = []

for i in range(N):
    counter = 0
    for j in range(N):
        if (abs(X[i] - X[j]) >= D):
            counter += 1
    if (counter == (N-1)):
        people_standing_apart.append(i+1)

count = len(people_standing_apart)
print(count)
for i in people_standing_apart:
    print(i, end=" ")
