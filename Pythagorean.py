#if Q is true a or b (whichevers bigger) is hypotonuse
#if Q is false c is hypotonuse
import math

def theorem(a,b,Q):
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
    return answer


print(theorem(3,5,False))