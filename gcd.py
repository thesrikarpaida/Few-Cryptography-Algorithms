# Finding the Greatest Common Divisor (gcd) of 2 numbers using the Euclidean Algorithm

print("--------------------\n--------------------\n--------------------\n")
print("In this program, we will find the gcd of 2 numbers using the Euclidean Algorithm.\n")
print("---------------------------------------------------------------------------------\n")

a, b = input("Enter the 2 integers, space separated:\n").split()
a, b = int(a), int(b)
r1, r2 = max(a,b), min(a,b)

while r2 > 0:
    r = r1%r2
    r1 = r2
    r2 = r

print("--------------------\n--------------------\n--------------------\n")
print("We finally get:",end=" ")
print("gcd(",a,",",b,") =",r1)
print("--------------------\n--------------------\n--------------------\n")