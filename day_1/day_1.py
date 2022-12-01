# https://adventofcode.com/2021/day/1#part2

prev=0
contador=-1
array_nums=[]

with open("e:/code/advent_code/2021/day_1/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        # Vamos a guardar los numeros en un array para la parte 2
        array_nums.append(int(linea))
        if(int(linea)>prev):
            contador=contador+1
        prev=int(linea)

print(contador)
print(len(array_nums))

# Aquí empieza la parte 2

sumita=0
prev2=0
contador2=-1

for n in range(len(array_nums)):
    if(n+2<len(array_nums)):
        sumita=array_nums[n]+array_nums[n+1]+array_nums[n+2]
    elif(n+1<len(array_nums)):
        sumita=array_nums[n]+array_nums[n+1]
    else:
        sumita=array_nums[n]
    if(sumita>prev2):
        contador2=contador2+1
    prev2=sumita
    
print(contador2)





