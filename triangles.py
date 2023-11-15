#Soh Cah Toa
# if Q is True y is numerator if Q is False y is denominator

import math

def Cos(d,y,Q):
    try:
        a = math.cos(d*math.pi/180)
        print(a)
    except:
        answer = f"Error\n{d}° doesnt have a cosine"
        return answer
    if Q == True:
        answer = y/a
        answer = round(answer,3)
    if Q == False:
        answer = y*a
        answer = round(answer,3)
    return answer
    
def Tan(d,y,Q):
    try:
        a = math.tan(d*math.pi/180)
    except:
        answer = f"Error\n{d}° doesnt have a tangent"
        return answer
    if Q == True:
        answer = y/a
        answer = round(answer,3)
    if Q == False:
        answer = y*a
        answer = round(answer, 3)
    return answer

def Sin(d,y,Q):
    try:
        a = math.sin(d*math.pi/180)
    except:
        answer = f"Error\n{d}° doesnt have a sine"
        return answer
    if Q == True:
        answer = y/a
        answer = round(answer,3)
    if Q == False:
        answer = y*a
        answer = round(answer, 3)
    return answer

# cos = y/x
print(Tan(60,24,True))