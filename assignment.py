#!python3
#Team Winners
import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

#made by Yurii Fadieiev

#Volume of a sphere
#Surface area of a sphere
#Factorial
#Find fibonacci number
#Interest calculations

def findSphereVolume():
    try: 
        r = float(input("Radius of the sphere: "))
        return round(4.0/3.0 * math.pi * r**3, 2)
    except Exception as e:
        return("Error. Bad input.")


def findSphereSurfaceArea():
    try:
        r = float(input("Radius of the sphere: "))
        return round(4 * math.pi * r**2, 2)
    except Exception as e:
        return("Error. Bad input.")

def findFactorial():
    try:
        n = int(input("Number to find the factorial of: "))
        f = 1
        for i in range(1, n+1):
            f = f * i
        return f
    except Exception as e:
        return("Error. Bad input.")

#print(', '.join(map(str, findFibonacciSequence()))) to be used for the below
def findFibonacciSequence():
    n = int(input("Enter the number of factors: "))

    out = []

    a = 0
    b = 1
    sum = a + b

    #count = 1

    while (a <= n):
    	out.append(a)

    	a = b
    	b = sum
    	sum = a + b

    return out

#P(1 + r/n)nt
def findCompoundInterest():
    p = float(input("Principal: "))
    r = float(input("Rate: "))
    n = float(input("Compound periods per year: "))
    t = float(input("Years: "))

    return round(p * (1 + (r / 100) / n)**(n * t), 2)

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    print(findCompoundInterest())
    #main()