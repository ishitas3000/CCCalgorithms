def main():

	T = str(input())
	S = str(input())

	cyclicShifts = []



	def substring(a, b):
		firstIndex = a - 1
		endIndex = b
		cyclicShifts.append(S[firstIndex: endIndex] + S[firstIndex - 1: firstIndex])



	for x in range (len(S)):
		substring(2, len(S))
		S = cyclicShifts[x]

	isSinT = 0

	for x in range (0, len(cyclicShifts)):
		if cyclicShifts[x] in T:
			isSinT = 1

	if isSinT == 0:
		print ("no")
	else:
		print ("yes")


if __name__ == '__main__':
	main()