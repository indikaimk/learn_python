class Person():
    def __init__(self):
        self.fname = "Indika"
        self.lname = "Kodagoda"
        self.age = 37

    def __repr__(self):
        return "<Person Class - fname:{0} lname:{1} age:{2}".format(self.fname, self.lname, self.age)
    
    def __str__(self):
        return "<Person ({0} {1} is {2})".format(
            self.fname, self.lname, self.age
        )
    
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode("utf-8"))


def main():
    c1 = Person()

    print(str(c1))
    print(repr(c1))
    print("Formatted: {0}".format(c1))
    print(bytes(c1))

if __name__ == "__main__":
    main() 