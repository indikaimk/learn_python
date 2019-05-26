#take extreme care in using variable argument lists. If another argument is added before *args 
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def main():
    print(addition(5, 10, 30))
    s = [1, 2, 3]
    print(addition(*s))

if __name__ == "__main__":
    main()