N = int(input())

days = []

for i in range(N):
    days.append(input())

avail = []

for r in range(5):
    P = []
    num = 0
    for i in range(N):
        P.append(days[i][r])
    for i in range(len(P)):
        if P[i] == 'Y':
            num += 1
    avail.append(num)

maxNum = max(avail)

D = []
for i in range(len(avail)):
    if avail[i] == maxNum:
        D.append(i+1)

# output = 0
# if len(D) > 1:
#     for i in range(len(D)):
#         output += str(i)

output = str(D)
out = output.replace('[', '')
put = out.replace(']', '')
output = put.replace(" ", '')

print(output)