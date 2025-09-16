import math
def turbine_power(v):
    if(v > 20):
        print("Error, velocity is too high, no power generated")
        P = 0
        return P
    if(v < 4):
        print("Error, velocity is too low, no power generated")
        P = 0
        return P
    A = math.pi*50**2
    P = 0.5*1.23*A*v**3*0.4
    return P
