scores = {"A": 0, "B": 0, "C": 0}

for _ in range(3):
    comparison = input()
    left, symbol, right = comparison[0], comparison[1], comparison[2]

    if symbol == ">":
        higher, lower = left, right
    else:
        higher, lower = right, left

    scores[higher] += 1
    scores[lower] -= 1

ordered = sorted(scores.items(), key=lambda pair: pair[1])

if len({value for _, value in ordered}) < 3:
    print("Impossible")
else:
    print("".join(letter for letter, _ in ordered))