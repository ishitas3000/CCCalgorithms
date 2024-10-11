import random
tests = random.randint(10,30)

scores = []
sum = 0
for i in range(tests):
    n = random.randint(50,100)
    scores.append(n)
    sum += n

avg = round(sum / tests, 2)
print("Class average: ", avg, "%")