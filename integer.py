def convertToTernary(N):
	if (N == 0):
		return
	x = N % 3
	N //= 3
	if (x < 0):
		N += 1
	convertToTernary

	if (x < 0):
		print(x + (3 * -1), end = "")
	else:
		print(x, end = "")


def convert(Decimal):
	
	print("Ternary number of ", Decimal,
		" is: ", end = "")

	if (Decimal != 0):
		convertToTernary(Decimal)
	else:
		print("0", end = "")


convert(int(input("enter Decimal:  ")))
