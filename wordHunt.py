word = input()
W = int(input())
R = int(input())

ws = []

for i in range(W):
    row = input()
    for i in range(len(row)):
        row = row.replace(' ', '')
    row = list(row)
    ws.append(row)

complete = 0

for i in range(len(ws)):
    for r in range(R):
        searching = 0
        for n in range(len(word)):
            char = ws[i][r]
            if char == word[n]:
                searching += 1
            else:
                break
        if searching == len(word):
            complete += 1
    

def findChar(char, r, l):
    while searching < len(word):
        if ws[r-1][l-1] == char:
            searching += 1
            char = word[(word.index(char)) + 1]
            r = ws[(ws.index(char))]
            findChar(char, r, l)


for r in range(len(ws)):
    for l in range(R):
        for n in range(len(word)):
            letter = ws[r][l]
            char = word[n]
            if letter == char:
                searching += 1
                char = word[n+1]
                findChar(char, r, l)
            else:
                searching = 0
                pass



for i in range(len(word)):
    ltr = word[i]
    if ws[n][r] == ltr:
        searching += 1
        if n > 0 and r > 0:
            if ws[n-1][r-1] == word[i+1]:
                searching += 1
            elif ws[n-1][r] == word[i+1]:
                searching += 1
            elif ws[n-1][r+1] == word[i+1]:
                pass