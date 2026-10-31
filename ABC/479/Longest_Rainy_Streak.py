# https://atcoder.jp/contests/abc479/tasks/abc479_b

N = input()
N = int(N)

S = input()

rainy_days_counter = 0
all_rainy_streak = [0]
for s in S:
    if (s == 'R'):
        rainy_days_counter += 1
    else:
        rainy_days_counter = 0

    if (rainy_days_counter != 0):
        all_rainy_streak.append(rainy_days_counter)


longest_rainy_streak = max(all_rainy_streak)
print(longest_rainy_streak)
