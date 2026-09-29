1
r = float(input("Enter circle radius:"))
s = r*r*3.14
print("Circle area =",s)

2
c = float(input("Enter the temperature in Celsius:"))
f = c*1.8+32
print( c,"(C) = ", f,"(F)")

3
n = int(input("Enter a number:"))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is a not prime number")    
      
4
n = int(input("Enter a number:"))
total = 0
for i in range(1, n):
    if n % i == 0:
        total = total + i
if total == n:
    print(n, "is a perfect number")
else:
    print(n, "is a not perfect number")

5
colors = ["Red","Blue","Green","Yellow"]
color = input("What is your favorite color:")
if color in colors:
    index = colors.index(color)
    print("Your colod is at index",index,"in my list")
else:
    print("Sorry, I could not find your color")

6
print(list(range(7)))
print(list(range(1, 11, 3)))
print(list(range(5, 0, -1)))
print(list(range(6, -3, -2)))

7
def remove_dollar_sign(s):
    return s.replace("$", "")

8
def extract_even(l):
    result = []
    for i in l:
        if i%2==0:
            result.append(i)