# https://adventofcode.com/2021/day/3#part2
import math

str_array=[]
gamma_bin=[]
gamma=0
epsilon=0
suma=(-1)*len(open("e:/code/advent_code/2021/day_3/input.txt").readlines())/2
aux=suma

for n in range(12):
    print(n)
    with open("e:/code/advent_code/2021/day_3/input.txt") as archivo:
        for linea in archivo:
            if(n==0):
                str_array.append(linea)
            suma= suma + int(linea[n])
        if(suma<0):
            gamma_bin.append(0)
        else:
            gamma_bin.append(1)
        print(suma)
        suma=aux

print(gamma_bin)
for n in range(len(gamma_bin)):
    gamma=gamma+gamma_bin[n]*(2**(len(gamma_bin)-1-n))

print("Gamma: ",gamma)

for n in range(len(gamma_bin)):
    if(gamma_bin[n]==0):
        epsilon=epsilon+(2**(len(gamma_bin)-1-n))

print("Epsilon: ",epsilon)

print("Multiplication: ",epsilon*gamma,"\n\n\n")


# Aquí empieza la parte 2
for n in range(len(str_array)):     #Here we are removing the \n in the end of each element of the array str_array
    str_array[n]=str_array[n][:len(str_array[n])-1]


oxygen_gen=str_array
ox_aux=[]
co2_scrub=str_array
co2_aux=[]
aux=0
most_common_ox=[]
least_common_co2=[]


for n in range(12):
    if(len(oxygen_gen)!=1):
        aux=len(oxygen_gen)
        for m in oxygen_gen:
            aux=aux-int(m[n])
        if(aux<len(oxygen_gen)/2) or (math.isclose(aux,len(oxygen_gen)/2)):
            most_common_ox.append(1)
        elif(aux>len(oxygen_gen)/2):
            most_common_ox.append(0)
        
        for m in oxygen_gen:
            if(int(m[n])==most_common_ox[n]):
                ox_aux.append(m)
        oxygen_gen=ox_aux
        ox_aux=[]
        print(most_common_ox)
        print(len(oxygen_gen))
        print("mas",oxygen_gen)
    else:
        print("LA SOLUCION DEL OXIGENO ES ", oxygen_gen)


    if(len(co2_scrub)!=1):
        aux=len(co2_scrub)
        for m in co2_scrub:
            aux=aux-int(m[n])
        if(aux<len(co2_scrub)/2) or (math.isclose(aux,len(co2_scrub)/2)):
            least_common_co2.append(0)
        elif(aux>len(co2_scrub)/2):
            least_common_co2.append(1)
        
        for m in co2_scrub:
            if(int(m[n])==least_common_co2[n]):
                co2_aux.append(m)
        co2_scrub=co2_aux
        co2_aux=[]
        print(least_common_co2)
        print(len(co2_scrub))
        print("menos",co2_scrub)
    else:
        print("LA SOLUCION DEL CO2 ES ", co2_scrub)

print("oxygen_gen: ",oxygen_gen)
print("co2_scrub: ", co2_scrub)

ox_binario=oxygen_gen[0]
co2_binario=co2_scrub[0]
ox_fin=0
co2_fin=0


for n in range(len(ox_binario)):
    ox_fin=ox_fin+int(ox_binario[n])*(2**(len(ox_binario)-1-n))
        
for n in range(len(co2_binario)):
    co2_fin=co2_fin+int(co2_binario[n])*(2**(len(co2_binario)-1-n))

print("\n\n\nOx final: ", ox_fin)
print("\nCO2 final: ", co2_fin)
print("\n\nRespuesta final: ", ox_fin*co2_fin)


