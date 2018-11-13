# f(x) = f(x - 1) + 2 and where f(0) return 1

# f(3) = f(3 - 1) + 2
# 	   = f(2) + 2
# f(2) = f(2 - 1) + 2} + 2
#      = f(1) + 2} + 2
# f(1) = f(1 - 1) + 2} + 2] + 2
#      = f(0) + 2} + 2] + 2
# f(0) = f(1) + 2} + 2] + 2
#      = 7

def f(x):
	if x == 0:
		return 1
	else:
		return  f(x - 1) + 2
print(f(int(input("Enter a Integer Number: "))))


# Fibonacci sequence

def f(x):
	if x == 0:
		return 1
	else:
		return x * f(x - 1)
print(f(int(input("Enter a Integer Number for Fibonacci sequence: "))))