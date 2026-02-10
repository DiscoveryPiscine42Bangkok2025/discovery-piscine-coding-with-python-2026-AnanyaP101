#!/bin/python3

fnum = int(input("Enter the first number:\n"))
snum = int(input("Enter the second number:\n"))

print(f"{fnum} x {snum} = {fnum * snum}")
if (fnum * snum == 0):
	print("The result is positive and negative.")
elif (fnum * snum > 0):
	print("The result is positive.")
else:
	print("The result is negative.")