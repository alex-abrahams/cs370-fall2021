def PowerSin(x):
    '''
     sum, n = PowerSin(x)
     
     Computes an approximation of the sin function using a power series.
     
     Input:
      x    scalar value
      
     Output:
      sum  scalar value
      n    the number of terms used in the series
    '''
    n = 0
    sum = 0
    term = 1
    while (sum + term != sum):
        power = 2*n+1
        numerator = math.pow(int(x),power)
        denominator = math.factorial(power)
        term = numerator/denominator
        if (n % 2 == 1):
            term = -term
        sum = sum + term
        n += 1
    
    return sum, n