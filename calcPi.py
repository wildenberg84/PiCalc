# Gregory-Leibniz implementation
def calc(totalSteps):
    pi = 0.0
    
    for i in range(0, totalSteps):
        divBy = 1.0 + (i * 2)
        
        if i % 2 == 0:
            pi += (4.0 / divBy)
        else:
            pi -= (4.0 / divBy)
        
        print(pi)

# note this method takes forever to converge past 3.141
calc(100000)
