import collections
from collections import defaultdict

def main():
    fruits = ['apple', 'pear', 'bananas', 'cherry', 'avacado', 'apple']
    fruitCounter = {}

    for fruit in fruits:
        if fruit in fruitCounter:
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1
    print(fruitCounter)

    #default dictionary will initialize the value if key does not exist.
    fruitCounter2 = defaultdict(int)
    for fruit in fruits:
        fruitCounter2[fruit] += 1
    print(fruitCounter2)

    fruitCounter3 = defaultdict(lambda: 100)
    for fruit in fruits:
        fruitCounter3[fruit] += 1
    print(fruitCounter3)

if __name__ == "__main__":
    main()

