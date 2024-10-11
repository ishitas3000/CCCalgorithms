pepNum = int(input())

SHU = 0

for i in range(pepNum):
    chilli = input()
    if chilli == "Poblano":
        SHU += 1500
    elif chilli == "Mirasol":
        SHU += 6000
    elif chilli == "Serrano":
        SHU += 15500
    elif chilli == "Cayenne":
        SHU += 40000
    elif chilli == "Thai":
        SHU += 75000
    elif chilli == "Habanero":
        SHU += 125000

print(SHU)