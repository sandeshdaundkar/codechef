'''
Given a number check if it is prime or not
'''

from math import sqrt


def prime_number(n):
	end = int(sqrt(n)) + 1
	is_prime = True
	
	if n <= 1:
		is_prime = False
		print("Number less than or equal to 1")
		return

	for i in range(2, end):
		if n % i == 0:
			is_prime = True
			break;

	if is_prime:
		print("Prime Number.")
	else:
		print("Not a prime number.")

prime_number(1)