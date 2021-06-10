# Modular Multiplicative Inverse
# We will find b = a^(-1) mod n or a*b = 1 mod n

print("--------------------\n--------------------\n--------------------\n")
print("We will find the Modular Multiplicative Inverse of a number.\n")
print("------------------------------------------------------------\n")

n = int(input("Enter the value of n:\n"))
print("Remember that the number you want to find the inverse of should be less than the modulus.")
a = int(input("Enter the value you want to find the inverse of:\n"))

r1, r2 = n, a
t1, t2 = 0, 1

while r2 > 0:
    q = r1//r2
    r = r1%r2
    r1 = r2
    r2 = r

    t = t1 - q*t2
    t1 = t2
    t2 = t

# The modular multiplicative inverse exists only if the gcd of a and n is 1
if r1 != 1:
    print("The inverse of",a,"mod",n,"does not exist, since the gcd(",n,",",a,"=",r1,"which is clearly greater than 1.")
else:
    print("The inverse of",a,"mod",n,"=",t1%n)