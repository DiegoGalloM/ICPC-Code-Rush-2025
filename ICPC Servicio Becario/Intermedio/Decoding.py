n = int(input())
two = input()
code = list(two)

answer = []

for i in reversed(range(len(code))):
    if len(answer) == 0:
        answer.append(code[i])
    else:
        if len(code)%2 == 0: #Si es par
            index = len(answer)//2
            answer.insert(index,code[i])
        else: # Si es impar
            index = len(answer)//2
            answer.insert(index, code[i])

answer = "".join(answer)
print(answer)
