def main():
	totalPlayers = int(input())
	a1 = 0
	a2 = 0
	b1 = 0
	b2 = 0
	c1 = 0
	c2 = 0
	d1 = 0
	d2 = 0
	e1 = 0
	e2 = 0
	f1 = 0
	f2 = 0
	g1 = 0
	g2 = 0
	h1 = 0
	h2 = 0
	i1 = 0
	i2 = 0
	j1 = 0
	j2 = 0

	if totalPlayers == 1:
		a1 = int(input())
		a2 = int(input())
	elif totalPlayers == 2:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
	elif totalPlayers == 3:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
	elif totalPlayers == 4:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
		d1 = int(input())
		d2 = int(input())
	elif totalPlayers == 5:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
		d1 = int(input())
		d2 = int(input())
		e1 = int(input())
		e2 = int(input())
	elif totalPlayers == 6:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
		d1 = int(input())
		d2 = int(input())
		e1 = int(input())
		e2 = int(input())
		f1 = int(input())
		f2 = int(input())
	elif totalPlayers == 7:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
		d1 = int(input())
		d2 = int(input())
		e1 = int(input())
		e2 = int(input())
		f1 = int(input())
		f2 = int(input())
		g1 = int(input())
		g2 = int(input())
	elif totalPlayers == 8:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
		d1 = int(input())
		d2 = int(input())
		e1 = int(input())
		e2 = int(input())
		f1 = int(input())
		f2 = int(input())
		g1 = int(input())
		g2 = int(input())
		h1 = int(input())
		h2 = int(input())
	elif totalPlayers == 9:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
		d1 = int(input())
		d2 = int(input())
		e1 = int(input())
		e2 = int(input())
		f1 = int(input())
		f2 = int(input())
		g1 = int(input())
		g2 = int(input())
		h1 = int(input())
		h2 = int(input())
		i1 = int(input())
		i2 = int(input())
	elif totalPlayers == 10:
		a1 = int(input())
		a2 = int(input())
		b1 = int(input())
		b2 = int(input())
		c1 = int(input())
		c2 = int(input())
		d1 = int(input())
		d2 = int(input())
		e1 = int(input())
		e2 = int(input())
		f1 = int(input())
		f2 = int(input())
		g1 = int(input())
		g2 = int(input())
		h1 = int(input())
		h2 = int(input())
		i1 = int(input())
		i2 = int(input())
		j1 = int(input())
		j2 = int(input())
	fergusonballRatings(totalPlayers, a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2, g1, g2, h1, h2, i1, i2, j1, j2)

def fergusonballRatings(totalPlayers, a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2, g1, g2, h1, h2, i1, i2, j1, j2):
	allPlayersScore = [a1, b1, c1, d1, e1, f1, g1, h1, i1, j1,]
	allPlayersFaul = [a2, b2, c2, d2, e2, f2, g2, h2, i2, j2]

	points = []

	for x in range(0, totalPlayers):
		points.append((allPlayersScore[x]*5) - (allPlayersFaul[x]*3))

	howMany = []

	for x in range(len(points)):
		if points[x] > 40:
			howMany.append(1)

	sumOfFourties = 0

	for x in range(len(howMany)):
		sumOfFourties += howMany[x]

	if sumOfFourties == totalPlayers:
		sum_ = str(sumOfFourties)
		print (sum_ + "+")
	else:
		print (sumOfFourties)

if __name__ == '__main__':
	main()