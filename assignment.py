#!python3
#Team Winners
import math

""""
#Volume of a sphere
#Surface area of a sphere
#Factorial
#Find fibonacci number
#Interest calculations
"""
#made by Yurii Fadieiev

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

#the following is by John
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
                if inpex.lower() == "yes":
                    pass
                else:
                    title()
        except:
            print("wrong input")





                    










    return()







def title():
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()

    #test of Yurii's programs
    findCompoundInterest()
    findFactorial()
    findFibonacciSequence()
    findSphereSurfaceArea()
    findSphereVolume()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()