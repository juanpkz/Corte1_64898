def fcn_factorial(x):
    fact=1
    for i in range(1,x+1):
        fact *= i
    return(fact)


if __name__=="__main__":
    fcn_factorial(7)
