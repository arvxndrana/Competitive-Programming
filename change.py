N = input()
A_i = input().split()
A_i = [int(x) for x in A_i]

one_yen = ten_yen = hundred_yen = 0
change = [0, 0, 0]

def what_to_give(to_pay):
    to_give = 0
    if (to_pay < 1000):
        to_give = 1000
    elif (to_pay % 1000 == 0):
        to_give = to_pay
    else:
        to_give = (to_pay // 1000 + 1) * 1000

    return to_give

for a in A_i:
    G = what_to_give(a) - a
    hundred_yen = G // 100
    ten_yen = (G - hundred_yen * 100) // 10
    one_yen = (G - hundred_yen * 100 - ten_yen * 10)

    change[0] += one_yen
    change[1] += ten_yen
    change[2] += hundred_yen

for ans in change:
    print(ans, end=" ")
