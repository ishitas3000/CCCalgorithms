def main():
	firstNum = int(input("Please enter any integer."))
	secondNum = int(input("Please enter another integer."))
	thirdNum = int(input("Please enter a third integer."))
	fourthNum = int(input("Please enter a fourth integer."))
	fifthNum = int(input("Please enter a fifth integer."))
	sixthNum = int(input("Please enter a sixth integer."))
	seventhNum = int(input("Please enter a seventh integer."))
	eighthNum = int(input("Please enter a eighth integer."))
	ninthNum = int(input("Please enter a ninth integer."))
	tenthNum = int(input("Please enter a final integer."))
	bubbleSort(firstNum, secondNum, thirdNum, fourthNum, fifthNum, sixthNum, seventhNum, eighthNum, ninthNum, tenthNum)

def bubbleSort(firstNum, secondNum, thirdNum, fourthNum, fifthNum, sixthNum, seventhNum, eighthNum, ninthNum, tenthNum):
	numbers = [firstNum, secondNum, thirdNum, fourthNum, fifthNum, sixthNum, seventhNum, eighthNum, ninthNum, tenthNum]
	print (numbers)
	for x in range(len(numbers)-1):
		if numbers[x] > numbers[x + 1]:
			numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
			print (numbers)

		else:
			break
	for x in range(len(numbers)-1):
		for x in range(len(numbers)-1):
			for x in range(len(numbers)-1):
				if numbers[x] > numbers[x + 1]:
					numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
					print (numbers)
				else:
					break
	print ("And that's the end! So the list is "+str(numbers[0])+", "+str(numbers[1])+", "+str(numbers[2])+", "+str(numbers[3])+", "+str(numbers[4])+", "+str(numbers[5])+", "+str(numbers[6])+", "+str(numbers[7])+", "+str(numbers[8])+", "+str(numbers[9])+".")



if __name__ == '__main__':
	main()