def main():
	input1 = str(input())
	tunings(input1)

def tunings(input1):
	str1 = ''
	chars = list(input1)
	for x in range(len(chars)): 
		if chars[x].isdigit() and chars[x+1].isalpha():
			for i in range(0, chars.index(x)-1):
				str1 += chars[i]
	print (str1)


if __name__ == '__main__':
	main()