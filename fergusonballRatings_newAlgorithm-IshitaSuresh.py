totalPlayers = int(input())
starPlayers = 0

for x in range (0, totalPlayers):
	plusPoints = int(input())
	foulPoints = int(input())
	totalScore = (plusPoints * 5) - (foulPoints * 3)
	#print ('the total score of one player: ' + str(totalScore))

	if totalScore > 40:
		starPlayers += 1
		#print ('found starPlayers')

#print ('outside of loop ' + str(starPlayers))
if starPlayers == totalPlayers:
	print (str(starPlayers) + '+')
else:
	print (starPlayers)


