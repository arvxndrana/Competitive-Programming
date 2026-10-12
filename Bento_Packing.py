### INCOMPLETE       ###
### WORK IN PROGRESS ###

import itertools

N, W = input().split()

N = int(N)
W = int(W)
A = [] # Deliciousness
B = [] # Volume
for i in range(N):
    a,b = input().split()
    a = int(a)
    b = int(b)

    A.append(a)
    B.append(b)

index_of_B = [i for i in range(N)]

all_combinations_of_B = []
all_combinations_of_index_of_B = []

for k in range(N):
    all_combinations_of_B.append(itertools.combinations(B,k))
    all_combinations_of_index_of_B.append(itertools.combinations(index_of_B,k))

better_all_combinations_of_B = []
better_all_combinations_of_index_of_B = []

for o in all_combinations_of_B:
    for t in o:
        better_all_combinations_of_B.append(t)

for o in all_combinations_of_index_of_B:
    for t in o:
        better_all_combinations_of_index_of_B.append(t)

acceptable_volume = []
acceptable_index = []

for i,k in enumerate(better_all_combinations_of_B):
    if (sum(t) <= W):
        acceptable_volume.append(t)
        acceptable_index.append(i)

optimized_acceptable_volume = acceptable_volume[N+1:]
optimized_acceptable_index = acceptable_index[N+1:]
print(optimized_acceptable_volume)
print(optimized_acceptable_index)

# all_deliciousness = []
# for t in optimized_acceptable_volume:
#     deliciousness = 0
#     for i in t:
#         deliciousness += A[i]
#     all_deliciousness.append(deliciousness)
# 
# maximum_deliciousness = max(deliciousness)
# print(maximum_deliciousness)

### INCOMPLETE       ###
### WORK IN PROGRESS ###
