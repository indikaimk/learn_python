def myFunc(x, y=None):
    """myFunc(x, y=None) --> Does not really do anything.

    Parameters:
    x: anything.
    y: can be nothing.
    """
    print(x)


def main():
    myFunc("x")
    print(myFunc.__doc__)

if __name__ == "__main__":
    main()
