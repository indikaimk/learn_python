def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squreFunc(x):
    return x**2

def toGrades(x):
    if (x >= 90):
        return "A"
    elif (x >=80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x>= 60 and x < 50):
        return "D"
    else:
        return "F"

def main():
    nums = (1, 2, 4, 5, 29, 30, 34, 47, 48, 53, 67, 72, 88, 93, 100)
    chars = "abcdEFgHiJkLMnOP"
    grades = (80, 78, 83, 92, 90, 84, 99, 75)

    #using fiter
    odds = list(filter(filterFunc, nums))
    print(odds)

    #using filters on characters
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    #using map() to create squares
    squares = list(map(squreFunc, nums))
    print(squares)

    #using map() to map integers to chracters
    grades = sorted(grades)
    gradeLetters = list(map(toGrades, grades))
    print(gradeLetters)

if __name__ == "__main__":
    main()