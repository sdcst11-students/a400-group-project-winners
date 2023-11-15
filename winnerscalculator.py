#This is the function that allows to run the calculator
""""
Made by: Yurii, John, Tyler (Team Winners)
"""

import math


#the following are by Yurii:
def findSphereVolume():
    while True: 
        try: 
            r = float(input("Radius of the sphere: "))
            print(f"The volume of the sphere is: {round(4.0/3.0 * math.pi * r**3, 2)}") 
            break
        except Exception as e:
            print("Error. Bad input.")


def findSphereSurfaceArea():
    while True:
        try:
            r = float(input("Radius of the sphere: "))
            print(f"The surface area of the sphere is: {round(4 * math.pi * r**2, 2)}")
            break
        except Exception as e:
            print("Error. Bad input.")

def findFactorial():
    while True:
        try:
            n = int(input("Number to find the factorial of: "))
            f = 1
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

            x = str(input("if Q is True y is numerator if Q is False y is denominator (t/f): "))
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

            x = str(input("if Q is True y is numerator if Q is False y is denominator (t/f): "))
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

            x = str(input("if Q is True y is numerator if Q is False y is denominator (t/f): "))
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

def Basmath():
    while True:
        try:
            inp1 = input("would u like to:\n---Add---\n---Sub---\n---Div---\n---Mul---\nEnter: ")
            while True:
                try:
                    if inp1 == "Add" or inp1 == "add":
                        while True:
                            try:
                                Add1 = float(input('input a number: '))
                                Add2 = float(input("input a second number: "))
                                print(Add1 + Add2)
                                break
                            except:
                                print("")
                    elif inp1 == "Sub" or inp1 == "sub":
                        while True:
                            try:
                                Sub1 = float(input('input a number: '))
                                Sub2 = float(input("input a second number: "))
                                print(Sub1 - Sub2)
                                break
                            except:
                                print("")
                    elif inp1 == "Div" or inp1 == "div":
                        while True:
                            try:
                                Div1 = float(input('input a number: '))
                                Div2 = float(input("input a second number: "))
                                print(Div1 / Div2)
                                break
                            except:
                                print("")
                    elif inp1 == "Mul" or inp1 == "mul":
                        input("""Hello Everybody my name is Multiplier
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
                        while True:
                            try:
                                Mul1 = float(input('input a number: '))
                                Mul2 = float(input("input a second number: "))
                                print(Mul1 * Mul2)
                                break
                            except:
                                print("")
                    pass            
                except:
                    print("Error, try again")
                inpex = input("Would you like to do another math? (Yes/No): ")
                if inpex == "yes" or inpex == "Yes":
                    pass
                elif inpex == "no" or inpex == "No":
                    return(main())
                else:
                    main()
        except:
            print("wrong input")   

def Sqrt():
    while True:
        try:
            a = float(input("Number: "))

            print(f"The square root is: {math.sqrt(a)}")
            break
        except Exception as e:
            print("Error. Bad input.")

def Expo():
    while True:
        try:
            exp1 = float(input("Number1: "))
            exp2 = float(input("Number2: "))

            print(f"The exponent of the two numbers is: {exp1**exp2}")
            break
        except Exception as e:
            print("Error. Bad input.")

#the main functions and loops
def main():
    print("""                                             
         ______   ______   ______   ______   ______ /  \    /  \ ____ |  |      ____  ____   _____   ____    ______   ______   ______   ______     ______ 
        /_____/  /_____/  /_____/  /_____/  /_____/ \   \/\/   // __ \|  | _/   ___\/  _ \ /     \_/ __ \  /_____/  /_____/  /_____/  /_____/  /_____/ 
        /_____/  /_____/  /_____/  /_____/  /_____/  \        /\  ___/|  |_\    \__(  <_> )  Y Y  \  ___/  /_____/  /_____/  /_____/  /_____/  /_____/ 
                                                      \__/\  /  \___  >____/    \___  >____/|__|_|  /   \___   >                                                
                                                           \/       \/              \/            \/        \/                                                 
    """)

    while True:
        print("\nHere are the instructions: ")
        print("=" * 99)
        print("sv = find sphere volume; ssa = find sphere surface area; f = find factorial\nfs = find fibonacci sequence; ci = compound interest; p = find pyramid\npt = pythagoras theorem; pr = prism; cos = find cosine\ntan = find tangent; sin = find sine; sq = find square root\ne = find exponent; bm = do basic math; q = quit")
        print("=" * 99)

        i = input("Enter the program : ")
        if i == 'q':
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
        elif i == 'bs':
            Basmath()
        elif i == 'sq':
            Sqrt()
        elif i == 'e':
            Expo()
    

if __name__ == "__main__":
    main()