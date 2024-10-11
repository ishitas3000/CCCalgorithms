def main():


	bleh = int(input())


	allRoomTiles = []

	for i in range (0, bleh):
		allRoomTiles.append (str(input()).split(' '))
	
	print (allRoomTiles.index('9'))


	#smallTreat = int(input())
	#medTreat = int(input())
	#largeTreat = int(input())

	#treatFormula = smallTreat + (2 * medTreat) + (3 * largeTreat)

	#if treatFormula < 10:
	#	print ("sad")
	#else:
	#	print ("happy")


if __name__ == '__main__':
	main()