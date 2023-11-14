#!python3
# Volume Calculator
# Feel free to rename your variables
#hello john wazzup!!!!!!!!!!!!!!
#hello john wazzup!!!!!!!!!!!!!!
#hello john wazzup!!!!!!!!!!!!!!

from assignment import Basmath
import math
import os
def title():
    os.system('cls')
    input("""                                              __      __       .__                                                                            
  ______   ______   ______   ______   ______ /  \    /  \ ____ |  |   ____  ____   _____   ____    ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/ \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  /_____/  /_____/  /_____/  /_____/  /_____/ 
 /_____/  /_____/  /_____/  /_____/  /_____/  \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/  /_____/  /_____/  /_____/  /_____/  /_____/ 
                                               \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >                                             
                                                    \/       \/          \/            \/     \/                                              
                                                                                                                                             
 \nChoose:\nBasmath(+-*/)\nexponents\nSquare root\n
                                                                                                                                            """)
    inptit = input("Enter: ")
    while True:
        try:
            if inptit == "Basmath":
                Basmath()
            elif inptit == "exponents":
                Expo()
            elif inptit == "Square root":
                Sqrt()
            """elif inptit == add your function

            elif inptit == add your function

            elif inptit == add your function

            elif inptit == add your function"""

            
        
            
        except:
            print("")





    return None


def Sqrt():
    sq1 = float.input("Number1: ")
    
    
    
    print(math.sqrt(sq1))


    return
def Expo():
    exp1 = float.input("Number1: ")
    exp2 = float.input("Number2: ")

    print(exp1**exp2)





    return()

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
    
    return None

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
                    return(title())
                else:

                    title()
        except:
            print("wrong input")





                    










    return()



main()









if __name__ == "__main__":
    main()
