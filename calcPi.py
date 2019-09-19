# Gregory-Leibniz implementation
def calcGregLeib(totalSteps):
    pi = 0.0
    
    for i in range(0, totalSteps):
        divBy = 1.0 + (i * 2)
        
        if i % 2 == 0:
            pi += (4.0 / divBy)
        else:
            pi -= (4.0 / divBy)
        
    print(pi)

calcGregLeib(1000000)


# Nilakantha implementation
def calcNilak(totalSteps):
    pi = 3.0
    
    for i in range(1, totalSteps):
        
        divBy = (i * 2) * (i * 2 + 1) * (i * 2 + 2)
        
        if i % 2 == 0:
            pi -= (4.0 / divBy)
        else:
            pi += (4.0 / divBy)
        
    print(pi)


calcNilak(1000000)


# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
# Chudnovsky implementation
from decimal import Decimal as Dec, getcontext as gc

def calcChud(maxIter = 70, prec = 1003, disp = 1002): # parameter defaults chosen to gain 1000 digits after the comma
    gc().prec = prec
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxIter + 1):
        M = (K**3 - 16*K) * M // k**3 
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp]) # drop few digits of precision for accuracy
    print("PI(maxIter={} iterations, gc().prec={}, disp={} digits) =\n{}".format(maxIter, prec, disp, pi))
    return pi

calcChud()
