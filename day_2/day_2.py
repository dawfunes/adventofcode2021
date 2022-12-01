# https://adventofcode.com/2021/day/2#part2

horizontal=0
depth=0
num=0

with open("e:/code/advent_code/2021/day_2/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        if(linea[0]=="f"):
            num=int(linea.replace("forward ",""))
            horizontal=horizontal+num
        elif(linea[0]=="d"):
            num=int(linea.replace("down ",""))
            depth=depth+num
        else:
            num=int(linea.replace("up ",""))
            depth=depth-num

print("Horizontal: ",horizontal)
print("Depth: ", depth)
print("Multiplicacion: ",horizontal*depth,"\n\n\n")

# Aquí empieza la parte 2

horizontal=0
depth=0
aim=0
num=0

with open("e:/code/advent_code/2021/day_2/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        if(linea[0]=="f"):
            num=int(linea.replace("forward ",""))
            horizontal=horizontal+num
            depth=depth+(num*aim)
        elif(linea[0]=="d"):
            num=int(linea.replace("down ",""))
            aim=aim+num
        else:
            num=int(linea.replace("up ",""))
            aim=aim-num

print("Part 2:")
print("Horizontal: ",horizontal)
print("Depth: ", depth)
print("Multiplicacion: ",horizontal*depth)