def main():
	bp = int(input())
	calulatePressure(bp)

def calulatePressure(b):
	# print ("I am inside.")
	if b >= 80 and b <= 200:
		p = (b * 5) - 400
		print (p)
		if p < 100:
			print (1)
		elif p == 100:
			print (0)
		else:
			print (-1)
	else:
		print ("Sorry, the input number must be greater than 80, and less than 200.")


if __name__ == '__main__':
	main()

