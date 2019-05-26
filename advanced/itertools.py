import itertools

def testFunc(z):
    if (z < 40):
        return True
    else:
        return False


def main():
    # cycle() iterator to cycle around a list
    seq1 = ["joe", "john", "mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # counting
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    
    #accumulate() create an iterator that accumulate
    vals = [10, 20, 100, 30, 150, 50, 50, 50, 20]
    acc = itertools.accumulate(vals)
    print(list(acc))
    #from the append the max value
    acc2 = itertools.accumulate(vals, max)
    print(list(acc2))

    #chain() function
    x = itertools.chain("ABCD", "1234", "abcd")
    print(list(x))

    #filter()
    a = itertools.dropwhile(testFunc, vals)
    b = itertools.takewhile(testFunc, vals)
    print(list(a))
    print(list(b))



if __name__ == "__main__":
    main()