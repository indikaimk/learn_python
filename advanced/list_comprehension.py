def main():
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17]

    #using map()
    evenSquared = list(
        map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens))
    )
    print(evenSquared)

    #using comprehensions
    print("using comprehensions")
    evenSquared2 = [e**2 for e in evens]
    print(evenSquared2)

    #using preicates
    oddsSquared = [e ** 2 for e in odds if e > 5 and e < 17]
    print(oddsSquared)

if __name__ == "__main__":
    main()
