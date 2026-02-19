cities = input()
criminals = input()

arr_cities = list(map(int, cities.split(" ")))
arr_criminals = list(map(int, criminals.split(" ")))

start = arr_cities[1]
n = arr_cities[0]
current_criminals = 0
distance = 0

if arr_criminals[start-1] == 1:
    current_criminals += 1
else:
    current_criminals = 0
    
while True:
    distance += 1

    left = start - distance
    right = start + distance

    if left < 1 and right > n:
        break

    if (left >= 1 and right <= n) and (arr_criminals[left - 1] == 1) and (arr_criminals[right - 1] == 1):
        current_criminals += 2

    elif (left < 1) and (right <= n) and (arr_criminals[right - 1] == 1):
        current_criminals += 1
    elif (right > n) and (left >= 1) and (arr_criminals[left - 1] == 1):
        current_criminals += 1

print(current_criminals)