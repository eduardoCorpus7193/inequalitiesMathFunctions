import math

constant = 0
lineal = 0
square = 0

print("Lets solve a quadratic inequality\n")
numTerms = int(input("How many terms are in the first part of the inequation? "))

for i in range(numTerms):
	coef = int(input("Write the coeficent of the " + str(i+1) + " term "))
	x = int(input("Write a 0 if is a constant\nWrite a 1 if is a x^1 \nOr write a 2 if is a x^2 "))
	if x==0:
		constant+=coef
	elif x==1:
		lineal+=coef
	elif x==2:
		square+=coef
print(str(square)+"x² + "+str(lineal)+"x + "+str(constant))

typeOf = int(input("Choose the type of inequality writting the number that correspond\n1.-'>='\n2.-'<='\n3.-'>'\n4.-'<'"))
if typeOf==1:
	print("Your choose was: >=")
	ineqType = ">="
elif typeOf==2:
	print("Your choose was: <=")
	ineqType = "<="
elif typeOf==3:
	print("Your choose was: >")
	ineqType = ">"
elif typeOf==4:
	print("Your choose was: <")
	ineqType = "<"

constant2 = 0
lineal2 = 0
square2 = 0

numTerms = int(input("How many terms are in the second part of the inequation? "))
for i in range(numTerms):
	coef = int(input("Write the coeficent of the " + str(i+1) + " term "))
	x = int(input("Write a 0 if is a constant\nWrite a 1 if is a x^1 \nOr write a 2 if is a x^2 "))
	if x==0:
		constant2+=coef
	elif x==1:
		lineal2+=coef
	elif x==2:
		square2+=coef
print(str(square2)+"x² + "+str(lineal2)+"x + "+str(constant2))

print("\nThe inequation is: "+str(square)+"x² + "+str(lineal)+"x + "+str(constant)+" "+ineqType+" "+str(square2)+"x² + "+str(lineal2)+"x + "+str(constant2))
a=square+(square2*(-1))
b=lineal+(lineal2*(-1))
c=constant+(constant2*(-1))
print(str(a)+"x² + "+str(b)+"x + "+str(c))

while True:
	try:
		x1=(-b-(math.sqrt(pow(b,2)-(4*(a*c)))))/(2*a)
		break
	except ValueError:
		print("Oops! That was no valid number.")
		break
while True:
	try:
		x2=(-b+(math.sqrt(pow(b,2)-(4*(a*c)))))/(2*a)
		break
	except ValueError:
		print("Oops! That was no valid number.")
		break

aux = 0
if x1>x2:
	aux=x1
	x1=x2
	x2=aux

print("x1 = "+str(x1))
print("x2 = "+str(x2))

if(typeOf==1):
	print("(-∞, "+x1+"] U ["+x2+", ∞)")

if(typeOf==2):
	print("[ "+x1+" , "+x2+" ]")

if(typeOf==3):
	print("(-∞, "+x1+") U ("+x2+", ∞)")	

if(typeOf==4):
	print("( "+x1+" , "+x2+" )")