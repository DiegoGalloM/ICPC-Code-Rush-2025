n = input()
h = input()

#Map aplica una función de la izquierda a todos los valores de la derecha
arr = list(map(int, h.split(" "))) 

i = 0
max_lluvia = 1
current_valley = 1

#Obtener máximos y mínimos
while i < len(arr)-1:
    current_lluvia = current_valley
    while i < len(arr)-1 and arr[i+1] >= arr[i]:
        current_lluvia += 1
        i += 1
    while i < len(arr)-1 and arr[i+1] <= arr[i]:
        current_lluvia += 1
        if arr[i+1] == arr[i]:
            current_valley+=1
        else:
            current_valley = 1
        i +=1

    max_lluvia = max(max_lluvia, current_lluvia)

print(max_lluvia)
