#if Q is true a or b (whichevers bigger) is hypotonuse
#if Q is false c is hypotonuse
import math

def theorem(a,b,Q):
    if Q == False:
      c = (a**2)*(b**2)
      answer = math.sqrt(c)

