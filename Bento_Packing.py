### INCOMPLETE       ###
### WORK IN PROGRESS ###

import itertools

# Taking standard inputs
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

# Listing all the combinations

all_combinations_of_B = []
all_combinations_of_index_of_B = []

for k in range(2,N):
    all_combinations_of_B.append(itertools.combinations(B,k))
    all_combinations_of_index_of_B.append(itertools.combinations(index_of_B,k))

# Unpacking all the combinations

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

print(acceptable_volume)
print(acceptable_index)
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
