def main():
	rb = int(input())
	sb = int(input())
	cupcakeParty(rb, sb)

def cupcakeParty(rb, sb):
	regular = rb * 8
	small = sb * 3
	cupcakes = regular + small
	leftOver = cupcakes - 28
	print (leftOver)

if __name__ == '__main__':
	main()