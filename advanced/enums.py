from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    BANANA = 1
    ORANGE = 2
    WOODAPPLE = 3
    TOMATOE = 4
    PEAR = auto()
    #RED_DELICIOUS = 1

def main():
    print(Fruit.BANANA)
    print(type(Fruit.BANANA))
    print(repr(Fruit.BANANA))

    print(Fruit.BANANA.name, Fruit.BANANA.value)

    print(Fruit.PEAR.value)

    #enums are hashable
    myFruits = {}
    myFruits[Fruit.BANANA] = "Yellow ripe"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()