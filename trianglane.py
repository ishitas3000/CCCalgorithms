C = int(input())

clmn = []
tape = 0

for i in range(2):
    column = input()
    for r in range(len(column)):
        column = column.replace(" ", "")
    column = list(column)
    clmn.append(column)

for r in range(len(clmn)):
    for i in range(len(clmn[r])):
        c = clmn[r]
        if c[i] == '1':
            if i > 0 and c[i-1] == '1' or i < (len(c) - 1) and c[i+1] == '1':
                if i < (len(c) - 1) and c[i+1] == '1' or i > 0 and c[i-1] == '1':
                        tape += 1
                else:
                    tape += 2
            else:
                tape += 3
            if i % 2 == 0:
                if r == 0:
                    if clmn[1][i] == '1':
                        tape -= 1
                elif r == 1:
                    if clmn[0][i] == '1':
                        tape -= 1
print(tape)