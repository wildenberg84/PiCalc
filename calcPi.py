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

calcGregLeib(100000000)


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


calcNilak(100000000)
