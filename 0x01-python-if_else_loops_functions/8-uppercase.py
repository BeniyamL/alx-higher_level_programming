#!/usr/bin/python3
def uppercase(str):
	for c in str:
		asci = ord(c)
		if asci >= 97 and asci < 123:
			print("{0:c}".format(asci - 32), end = "")
		else:
			print(c, end = "")
	print()
