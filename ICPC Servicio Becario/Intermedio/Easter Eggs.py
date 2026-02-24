n = int(input())

colors = ["R", "O", "Y", "G", "B", "I", "V"]

output = []

if n < 7:
    for i in range(7):
        index = i%7
        output.append(colors[index])
else:
    for i in range(7):
        index = i%7
        output.append(colors[index])
    for j in range(7, n):
        index = 3 + ((j-7)%4)       
        output.append(colors[index])

output = "".join(output)

print(output)