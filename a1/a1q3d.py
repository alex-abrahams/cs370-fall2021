values = [math.pi/2, 11*math.pi/2, 21*math.pi/2, 31*math.pi/2]
print("computed value |exact value |number of terms |absolute error |relative error")
for x in values:
    powersinned = PowerSin(x)
    powersin = powersinned[0]
    terms = powersinned[1]
    exact = math.sin(x)
    abserr = abs(powersin-exact)
    relerr = abserr/abs(exact)
    print(powersin, "|", exact, "|", terms, "|", abserr, "|", relerr)