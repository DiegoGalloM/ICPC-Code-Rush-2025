n = (input())

nArr = list(n)
counter = 0
while len(nArr) != 1:
    acc = 0
    for digit in nArr:
        acc += int(digit)
    nArr = list(str(acc))
    counter +=1

print(counter)
