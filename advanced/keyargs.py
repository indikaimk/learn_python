def riskyFunction(a, b, suppressException=False):
    pass

def myFunction(a, b, *, suppressException=False):
    pass

def main():
    #riskyFunction may be invoked unknowingly passing different parameter to suppressException
    riskyFunction(1, 2, 3)
    myFunction(1, 2, suppressException=True)

if __name__ == "__main__":
    main()