P = int(input())
C = int(input())

points = P * 50
points -= C * 10

if P > C:
    points += 500

print(points)

