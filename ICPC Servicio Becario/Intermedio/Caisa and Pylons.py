n = int(input())
pylines = input()

arr_pylines = list(map(int, pylines.split(" ")))
arr_pylines.insert(0,0)

curr_energy = 0
dollars = 0
for i in range(len(arr_pylines)):
    if i != len(arr_pylines)-1:
        difference = arr_pylines[i+1] - arr_pylines[i]
        if difference > 0 and curr_energy == 0:
            dollars += difference
        elif difference > curr_energy:
            dollars += (difference-curr_energy)
            curr_energy = 0
        else:
            curr_energy -= difference

print(dollars)