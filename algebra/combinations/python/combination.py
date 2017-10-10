def fact(n):
	if n == 0:
		return 1
	else:
		return n* fact(n-1)

def combination(n, r):
	return fact(n)/(fact(r)*fact(n-r))

