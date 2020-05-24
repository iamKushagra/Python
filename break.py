# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)
# def factorial(n):
#    	if n == 1:
#    		return n
#    	else:
#    		return n*factorial(n-1)

# print("The factorial of 6 is", factorial(6))


# def fib(n):
# 	if n == 1 or n==2:
# 		return 1
# 	else:
# 		return fib(n-1)+fib(n-2)
# print("the fib is", fib(6))


def gcd(a,b):
	if a==b:
		return a
	elif a%b==0:
		return b
	elif b%a==0:
		return a
	elif a>b:
		return gcd(a%b, b)
	elif a<b:
		return gcd(a, b%a)

print("The gcd 105 and 91 is", gcd(105,91))