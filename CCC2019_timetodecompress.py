def main():


	numMessages = int(input())

	myMessage = []
	repeatTimes = 0
	endMessage = []
	messageLine = ""

	for i in range (numMessages):
		myMessage.append(str(input()).split(' '))
		repeatTime = int(myMessage[i][0])
		
		for x in range (repeatTime):
			messageLine += myMessage[i][1]
		endMessage.append(messageLine)
		messageLine = ""

	for x in range (0, len(endMessage)):
		print(endMessage[x])



if __name__ == '__main__':
	main()