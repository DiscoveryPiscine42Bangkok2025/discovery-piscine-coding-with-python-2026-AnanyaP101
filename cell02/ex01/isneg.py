#!/bin/python3

def main():
	n = int(input('input number : '))

	if (n == 0):
		print("This number is both positive and negative.")
	elif (n < 0):
		print("This number is negative.")
	else:
		print("This number is positive.")
main()