S = input()
new_S = S[0]

for a in S[1:]:
    new_S += 'o'
    new_S += a

print(new_S)
