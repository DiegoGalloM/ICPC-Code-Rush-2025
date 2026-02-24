import sys
read = sys.stdin.readline

n = int(read().strip())
prices = list(map(int, read().split()))
m = int(read().strip())

sorted_prices = sorted(prices)

prefix_prices = [0]
for val in prices:
    prefix_prices.append(prefix_prices[-1] + val)

prefix_sorted = [0]
for val in sorted_prices:
    prefix_sorted.append(prefix_sorted[-1] + val)

for _ in range(m):
    t, l, r = map(int, read().split())
    if t == 1:
        total = prefix_prices[r] - prefix_prices[l - 1]
    else:
        total = prefix_sorted[r] - prefix_sorted[l - 1]
    print(total)