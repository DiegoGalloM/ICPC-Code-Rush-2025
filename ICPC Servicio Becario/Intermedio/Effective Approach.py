n = int(input())
array = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

pos = {}
for i, val in enumerate(array, start=1):
    pos[val] = i

counterVasya = 0
counterPetya = 0
for q in queries:
    p = pos[q]
    counterVasya += p
    counterPetya += n - p + 1

print(counterVasya, counterPetya)