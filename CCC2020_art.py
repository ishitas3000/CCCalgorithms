def main():

	minX = 100000000000000000000      
	minY = 100000000000000000000
	maxX = -10000000000000000000
	maxY = -10000000000000000000

	coords = []

	paintDrops = int(input())

	for i in range (paintDrops):
		inputCoord = str(input())
		coords = (inputCoord.split(','))

		inputX = int(coords[0])
		inputY = int(coords[1])

		if inputX < minX:
			minX = inputX

		if inputY < minY:
			minY = inputY

		if inputX > maxX:
			maxX = inputX

		if inputY > maxY:
			maxY = inputY


	print (str(minX - 1) + "," + str(minY - 1))
	print (str(maxX + 1) + "," + str(maxY + 1))


if __name__ == '__main__':
	main()