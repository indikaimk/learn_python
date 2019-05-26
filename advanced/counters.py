from collections import Counter

def main():
    class1 = ["Bob", "Marc", "Jane", "Johanna", "Katy", "Tom"]
    class2 = ["Bill", "Marc", "Chan", "Jonny", "Katy", "Phil"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1['Jane'])
    print(sum(c1.values()), "students in class 1")
    c1.update(class2)
    print(sum(c1.values()), "students in class 1 after update")
    print(c1.most_common(3))

    c1.subtract(c2)
    print(sum(c1.values()), "students in class 1 after subtract")

    #fins values in both classes
    print(c1 & c2)

if __name__ == "__main__":
    main()