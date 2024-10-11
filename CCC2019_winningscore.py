def main():


	allPoints = []

	for i in range (6):
		allPoints.append(int(input()))

	applePoints = 3 * allPoints[0] + 2 * allPoints[1] + allPoints[2]
	bananaPoints = 3 * allPoints[3] + 2 * allPoints[4] + allPoints[5]

	if applePoints > bananaPoints:
		print ("A")
	elif applePoints < bananaPoints:
		print ("B")
	else:
		print ("T")




if __name__ == '__main__':
	main()