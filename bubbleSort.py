def main():
	firstNum = int(input("Please enter any integer."))
	secondNum = int(input("Please enter another integer."))
	thirdNum = int(input("Please enter a third integer."))
	bubbleSort(firstNum, secondNum, thirdNum)

def bubbleSort(firstNum, secondNum, thirdNum):
	numbers = [firstNum, secondNum, thirdNum]
	print (numbers)
	for x in range(len(numbers)-1):
		if numbers[x] > numbers[x + 1]:
			numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
			print (numbers)

		else:
			break
	for x in range(len(numbers)-1):
		if numbers[x] > numbers[x + 1]:
			numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
			print (numbers)
		else:
			break
	print ("And that's the end! So the list is "+str(numbers[0])+", "+str(numbers[1])+", "+str(numbers[2])+".")



if __name__ == '__main__':
	main()