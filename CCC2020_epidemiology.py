def main():


	P = int(input())
	N = int(input())
	R = int(input())


	infectedSoFar = 0
	eachDayInfected = 0
	days = 0

	while infectedSoFar <= P: 
		print ("------------")
		eachDayInfected = N*(R**days)
		infectedSoFar += eachDayInfected
		print ("on day " + str(days) + ", " + str(eachDayInfected) + " was infected, a total of " + str(infectedSoFar) + ".")
		days += 1

	print (days - 1)

if __name__ == '__main__':
	main()