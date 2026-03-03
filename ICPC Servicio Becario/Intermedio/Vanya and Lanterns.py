import sys
read = sys.stdin.readline

n, l = map(int, read().split())
lanterns = list(map(int, read().split()))
lanterns.sort()

first_gap = lanterns[0] - 0
last_gap = l - lanterns[n-1]
middle_gap = 0
for i in range(n):
    difference = lanterns[i] - lanterns[i-1]
    if difference > middle_gap:
        middle_gap = difference

ans = max(middle_gap/2,first_gap,last_gap)
print(f"{ans:.10f}")