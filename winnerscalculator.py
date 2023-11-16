#This is the function that allows to run the calculator
""""
Made by: Yurii, John, Tyler (Team Winners)
"""

import math
import os

#the following are by Yurii:
def findSphereVolume():
    while True: 
        try: 
            r = float(input("Radius of the sphere: "))

            if r < 0: raise Exception

            print(f"The volume of the sphere is: {round(4.0/3.0 * math.pi * r**3, 2)}") 
            break
        except Exception as e:
            print("Error. Bad input.")


def findSphereSurfaceArea():
    while True:
        try:
            r = float(input("Radius of the sphere: "))
            
            if r < 0: raise Exception

            print(f"The surface area of the sphere is: {round(4 * math.pi * r**2, 2)}")
            break
        except Exception as e:
            print("Error. Bad input.")

def findFactorial():
    while True:
        try:
            n = int(input("Number to find the factorial of: "))
            f = 1

            if n < 0: raise Exception

            for i in range(1, n+1):
                f = f * i
            print(f"The factorial is: {f}")
            break
        except Exception as e:
            print("Error. Bad input.")

#print(', '.join(map(str, findFibonacciSequence()))) to be used for the below
def findFibonacciSequence():
    while True:
        try:
            n = int(input("Enter the number to find the fibonacci sequence of: "))

            if n < 0:
                raise Exception

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

            print(f"The fibonacci sequence is: {', '.join(map(str, out))}")
            break
        except Exception as e:
            print("Error. Bad input.")

#P(1 + r/n)nt
def findCompoundInterest():
    while True:
        try:
            p = float(input("Principal: "))
            r = float(input("Rate: "))
            n = float(input("Compound periods per year: "))
            t = float(input("Years: "))

            if p < 0 or r < 0 or n < 0 or t < 0:
                raise Exception

            print(f"The interest is: {round(p * (1 + (r / 100) / n)**(n * t), 2)}")
            break
        except Exception as e:
            print("Error. Bad input.")


#the following are by Tyler ##########################################################
def pyramid():
    while True:
        try:
            l = float(input("Length: "))
            w = float(input("Width: "))
            h = float(input("Height: "))

            if l < 0 or w < 0 or h < 0:
                raise Exception
            
            print(f"The answer is: {(l*w*h)/3}")
            break
        except Exception as e:
            print("Error. Bad input.")

#####################erriririri ERRRORRRR ERORRR HEREHREHRHEREERHHRE ERRORR
def theorem():
    while True:
        try:
            x = input("Do you have the hypothenuse (t/f): ")
            if x == 't':
                Q = True
            elif x == 'f':
                Q = False

            a = float(input("Side a: "))
            b = float(input("Side b: "))    

            if a < 0 or b < 0:
                raise Exception   

            if Q == False:
              c = (a**2)*(b**2)
              answer = math.sqrt(c)
            if Q == True:
              if a > b:
                h = a
                s = b
              if b > a:
                h = b
                s = a
              c = (h**2)-(s**2)
              answer = math.sqrt(c)

            print(f"The answer is: {answer}")
            break
        except Exception as e:
            print("Error. Bad input.")

def prism():
    while True:
        try:
            x = float(input("X: "))
            y = float(input("Y: "))
            z = float(input("Z: "))

            if x < 0 or y < 0 or z < 0:
                raise Exception

            print(f"The answer: {x * y * z}")
            break
        except Exception as e:
            print("Error. Bad input.")

def Cos():
    while True:
        try:
            d = float(input("D: "))
            y = float(input("Y: "))
            a = math.cos(d*math.pi/180)

            x = str(input("Hypothenuse or angle (t/f): "))
            if x == 't':
                Q = True
            elif x == 'f':
                Q = False 

            if Q == True:
                answer = y/a
                answer = round(answer,3)
            if Q == False:
                answer = y*a
                answer = round(answer,3)

            print(f"The answer is: {answer}")
            break
        except Exception as e:
            print("Error. Bad input.")
    
def Tan():
    while True:
        try:
            d = float(input("D: "))
            y = float(input("Y: "))
            a = math.tan(d*math.pi/180)

            x = str(input("Hypothenuse or angle (t/f): "))
            if x == 't':
                Q = True
            elif x == 'f':
                Q = False 

            if Q == True:
                answer = y/a
                answer = round(answer,3)
            if Q == False:
                answer = y*a
                answer = round(answer,3)

            print(f"The answer is: {answer}")
            break
        except Exception as e:
            print("Error. Bad input.")

def Sin():
    while True:
        try:
            d = float(input("D: "))
            y = float(input("Y: "))
            a = math.cos(d*math.pi/180)

            x = str(input("Hypothenuse or angle (t/f): "))
            if x == 't':
                Q = True
            elif x == 'f':
                Q = False 

            if Q == True:
                answer = y/a
                answer = round(answer,3)
            if Q == False:
                answer = y*a
                answer = round(answer,3)

            print(f"The answer is: {answer}")
            break
        except Exception as e:
            print("Error. Bad input.")


#the following are by John ######################################################################################

def addition():
    while True:
        try:
            a = float(input("A: "))
            b = float(input("B: "))

            print(f"The sum of {a} and {b} is: {a + b}")
            break
        except Exception as e:
            print("Error. Bad input.")

def subtraction():
    while True:
        try:
            a = float(input("A: "))
            b = float(input("B: "))

            print(f"The difference of {a} and {b} is: {a - b}")
            break
        except Exception as e:
            print("Error. Bad input.")

def division():
    while True:
        try:
            a = float(input("A: "))
            b = float(input("B: "))

            print(f"The quotient of {a} and {b} is: {a / b}")
            break
        except Exception as e:
            print("Error. Bad input.")

def multiplication():
    while True:
        try:
            print("""Hello Everybody my name is Multiplier
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⡠⣴⣿⡿⢟⡿⠿⠗⠚⠛⣛⣶⣤⠒⡤⠤⢤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⡎⢠⢿⡥⢘⡥⣠⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠸⠽⠷⠦⢤⡤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠸⣷⣧⢏⡴⡿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢄⡈⠉⠛⠽⣶⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠴⢺⣽⣿⣿⣿⣾⢿⢦⢆⣤⣶⣖⠵⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠳⠦⣀⢀⠉⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣋⣅⣀⣾⣿⣿⣿⣿⣿⣷⣯⣾⣿⠟⠁⠀⣧⡾⡁⠠⢖⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠙⠷⣶⢆⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣵⣲⣴⣿⣼⣁⣴⡽⣱⠀⠀⠀⠈⡉⠠⣶⣶⣶⣴⡤⠠⢉⠺⣕⣿⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⡟⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⢡⣿⠠⢠⣢⣾⣻⠀⣀⠉⠉⠛⣿⣿⣶⣮⠻⣻⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠈⠈⠛⠿⢿⣿⣿⣿⣾⣿⣶⣿⣿⣿⣿⣿⣿⣅⠀⠀⢮⣿⣻⣿⣿⣬⣻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠉⠻⣿⣿⡿⢟⠻⢿⣿⣿⣿⣿⣿⡬⢣⢣⠻⣿⢻⣿⣻⣷⡙⢿⡀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠙⠛⠉⠁⠀⠀⢹⡿⣿⣿⣿⣳⡛⣿⣷⣽⣿⡹⣧⠻⢿⣆⣳⡀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢹⣿⣿⡏⡇⣿⣿⣿⣿⡄⠹⣧⠻⣎⡎⣿⡄⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣻⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣇⣿⣿⣿⣿⣿⣷⣀⣹⣆⢿⠹⡽⡅⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣯⣴⣦⣿⣿⣿⣿⣟⣁⣀⣀⠀⠀⣠⣥⣤⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⡀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⡚⡌⡇⠇⠇⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⢣⠃⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠻⠶⣮⣬⣭⣽⣄⣀⠈⢀⣴⣿⣿⣟⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠹⠇⠹⢻⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⢫⠔⢺⡿⢿⡟⠀⠀⠉⠛⠿⣇⡤⠤⣴⣛⠛⠿⠭⣿⣤⣿⠛⢻⣿⡿⠿⠿⠟⣿⣽⣿⠛⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀⠛⣳⠺⠁⠸⣧⠀⡀⠀⠀⠀⠀⣀⠀⠀⠀⠉⠙⠻⠋⣿⡧⠀⢸⣿⡏⠓⠒⠛⠋⠙⣼⢸⣿⠻⡻⣿⣿⣿⣿⣇⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⢢⡵⠦⣜⠀⣿⣧⠁⠀⠀⠀⠀⠀⠀⠉⠉⠉⢙⢟⠖⠊⠀⢸⠀⣿⣷⣧⠤⠴⠶⡶⢾⠟⢸⠂⡇⣿⣿⢿⣿⣷⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⡀⠀⠘⠷⢿⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⠀⠀⠀⠈⠀⣿⠙⡇⠀⠀⠀⠸⣾⡆⠀⠀⢸⠋⣿⣼⢹⣿⡄⢸⠿⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣌⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠂⠀⠀⠀⠀⠀⢻⢳⣷⡀⠀⠀⠀⣹⡇⠀⠀⠈⠀⠿⡏⢸⣸⠁⣼⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣐⣫⣿⡛⠀⠀⠀⠀⣀⣤⣶⣿⡟⢠⡀⠀⠀⠀⠀⢠⠆⠀⢧⣧⣳⣴⠄⢀⣿⡇⠀⠀⠀⠀⠚⠃⢸⡿⢡⡏⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣸⠀⠀⢰⣿⣯⣿⣥⣤⣤⣹⣶⣤⣄⠂⠊⣠⢠⣾⣿⣋⣿⣷⣌⣸⡇⠀⠀⠀⠀⠀⠀⠘⣻⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣀⣀⠀⠈⣿⣧⣿⠀⢠⠘⡇⣻⣿⣮⣟⣻⠿⣿⢿⣿⣷⣯⣶⣴⣿⣿⣿⣿⣇⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠛⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⡿⡄⢸⡹⠏⠀⠹⣮⡈⡟⢮⣿⠛⠛⣻⠿⣿⡿⢻⢫⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⢃⣿⣿⣿⡿⠿⣿⠘⣿⣧⣿⣷⣷⡂⢿⡀⠠⡓⠌⡷⣧⣇⠈⢻⢉⣧⣿⠛⡰⣳⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⡼⢿⡀⢸⣿⡿⢩⢂⣾⡇⠀⢻⣿⣿⣿⣿⢷⡎⠀⠀⠀⠀⠈⢎⢷⡟⠛⠿⡟⡿⠇⡇⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢼⠟⣠⢻⣾⣿⡇⠘⢸⡏⠀⠀⠘⣿⣿⣿⡏⠟⠁⠀⠀⠀⠀⠁⠊⠑⢾⣶⣴⣾⡏⢀⣷⣿⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⣠⣾⡗⠈⠘⣿⣿⣷⠀⠸⡇⠀⢠⠀⢚⣿⣿⣾⢯⡀⠀⠀⠀⠀⠀⠠⣓⣿⣿⣏⡟⠋⠈⢸⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣠⣾⢳⠹⣷⠙⠀⡼⣿⣿⠀⠀⢿⠁⠀⠇⠈⢻⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠛⡿⠉⠀⠀⠀⠘⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠈⢧⣽⣿⣷⠀⠀⢀⠀⠹⣿⡀⠀⠸⡇⢃⠀⠀⠀⢿⣿⣿⣦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠀⣇⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⢀⣴⣿⣿⣻⣿⣧⠀⢽⣫⢤⠹⣷⡄⠀⢹⡌⠆⠀⠀⠀⠻⣿⣿⣗⣀⡤⠠⣀⠄⣄⠀⢀⣾⡄⣳⣼⣯⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣶⣿⣿⣿⣿⣿⣮⣿⣿⣆⢯⡳⡜⢙⣿⣄⠀⢻⡞⠀⠀⠀⠀⠹⣿⣿⣿⣟⣽⣞⣿⣿⡷⢤⣿⣏⣷⣽⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⣨⡈⢿⣷⡌⢿⡄⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⡧⡌⢟⠿⣮⣻⣄⠀⠀⠀⠀⠀⠀⠙⠛⠉⠛⠿⠿⢟⡿⠛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣇⠈⠛⠿⣦⡀⠀⠀⠀⠀⠀⠀⣀⣩⡾⣠⠋⡼⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣷⣬⣿⣷⣦⣎⠉⠈⣡⠞⣋⠜⢫⡇⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢉⡙⣿⣿⣿⣤⡛⣡⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢀⡀⣀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡟⣮⢿⣿⣿⣿⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣠⣾⣯⣿⠋
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢿⣿⣿⣿⣿⣿⣿⣿⣿⠅⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⡆⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠉⠀⠀⠀
            """)
            a = float(input("A: "))
            b = float(input("B: "))

            print(f"The product of {a} and {b} is: {a * b}")
            break
        except Exception as e:
            print("Error. Bad input.")

def sqrt():
    while True:
        try:
            a = float(input("Number: "))

            print(f"The square root of {a} is: {math.sqrt(a)}")
            break
        except Exception as e:
            print("Error. Bad input.")

def expo():
    while True:
        try:
            a = float(input("A: "))
            b = float(input("B: "))

            print(f"The exponent of {a} and {b} is: {a**b}")
            break
        except Exception as e:
            print("Error. Bad input.")

#the main functions and loops
def main():
    os.system('cls')
    print("""                                             
         ______   ______   ______   ______   ______ /  \    /  \ ____ |  |     ____  ____   _____   ____    ______   ______   ______   ______   ______ 
        /_____/  /_____/  /_____/  /_____/  /_____/ \   \/\/   // __ \|  |   _/ ___\/  _ \ /     \_/ __ \  /_____/  /_____/  /_____/  /_____/  /_____/ 
        /_____/  /_____/  /_____/  /_____/  /_____/  \        /\  ___/|  |_  \  \__(  <_> )  Y Y  \  ___/  /_____/  /_____/  /_____/  /_____/  /_____/ 
                                                      \__/\  /  \___  >____/  \___  >____/|__|_|  / \___   >                                                
                                                           \/       \/            \/            \/        \/                                                 
    """)

    while True:
        print("\n\n\nHere are the instructions: ")
        print("=" * 99)
        print("sv = find sphere volume; ssa = find sphere surface area; f = find factorial\nfs = find fibonacci sequence; ci = compound interest\np = find pyramid pt = pythagoras theorem; pr = prism\ncos = find cosine; tan = find tangent; sin = find sine\nadd = addition; sub = subtraction div = division; mul = multiplication\nsq = square root; ex = exponent\nq = quit")
        print("=" * 99)

        i = input("Enter the program : ")
        if i == 'q':
            print("Bye bye!")
            break
        elif i == 'sv':
            findSphereVolume()
        elif i == 'ssa':
            findSphereSurfaceArea()
        elif i == 'f':
            findFactorial()
        elif i == 'fs':
            findFibonacciSequence()
        elif i == 'ci':
            findCompoundInterest()
        elif i == 'p':
            pyramid()
        elif i == 'pt':
            theorem()
        elif i == 'pr':
            prism()
        elif i == 'cos':
            Cos()
        elif i == 'tan':
            Tan()
        elif i == 'sin':
            Sin()
        elif i == 'add':
            addition()
        elif i == 'sub':
            subtraction()
        elif i == 'div':
            division()
        elif i == 'mul':
            multiplication()
        elif i == 'sq':
            sqrt()
        elif i == 'ex':
            expo()    

if __name__ == "__main__":
    main()