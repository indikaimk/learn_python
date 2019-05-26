def CelsiusToFarenthite(c):
    return (c * 9/5) + 32

def FarenhiteToCelsius(f):
    return (f - 32) *5/9

def main():
    ctemps = [25, 30, 40]
    ftemps = [32, 100, 212]

    #usging map() function in regular way.
    print(list(map(CelsiusToFarenthite, ctemps)))
    print(list(map(FarenhiteToCelsius, ftemps)))

    #using lambdas 
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))

if __name__ == "__main__":
    main()