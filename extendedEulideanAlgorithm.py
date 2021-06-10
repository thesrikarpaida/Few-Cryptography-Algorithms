# The Extended Eulidean Algorithm calculates the gcd(a,b) and at the same time
# find the value of s and t such that, s*a + t*b = gcd(a,b)

print("--------------------\n--------------------\n--------------------\n")
print("In this program, we will find the gcd of 2 numbers and the value of s and t using the Extended Euclidean Algorithm.\n")
print("---------------------------------------------------------------------------------\n")

a, b = input("Enter the 2 integers, space separated:\n").split()
a, b = int(a), int(b)

r1, r2 = max(a,b), min(a,b)
s1, s2 = 1, 0
t1, t2 = 0, 1

while r2 > 0:
    q = r1//r2
    r = r1%r2
    r1 = r2
    r2 = r

    s = s1 - q*s2
    s1 = s2
    s2 = s

    t = t1 - q*t2
    t1 = t2
    t2 = t

s, t = s1, t1

# The values we get satisfy the equation, s*a + t*b = gcd(a,b)

print("--------------------\n--------------------\n--------------------\n")
print("gcd(",a,",",b,") =",r1)
print("Also, the equation involving the 2 numbers and their gcd is:")
print(s,"*",a,"+",t,"*",b,"=",r1)