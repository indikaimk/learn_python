class Employee():
    def __init__(self, fname, lname, level, yearsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.yearsService = yearsService

    def __gt__(self, other):
        if self.level == other.level:
            return self.yearsService > other.yearsService
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.yearsService < other.yearsService
        return self.level < other.level

    def __eq__(self, other):
        return self.level == other.level

    def __repr__(self):
        return "<Employee name: {0} level: {1} yearsService: {2}>".format(
            self.fname, self.level, self.yearsService
        )


def main():
    dept = []
    dept.append(Employee("Johanna", "Smith", 2, 3))
    dept.append(Employee("Tim", "Blake", 4, 5))
    dept.append(Employee("Cate", "Frazer", 2, 4))
    dept.append(Employee("Tom", "Smith", 2, 3))
    dept.append(Employee("Jerry", "Game", 4, 10))
    dept.append(Employee("Mickey", "Mouse", 5, 3))
    
    print(dept[0] > dept[1])
    print(dept[2] < dept[3])
    print(dept[1] < dept[4])
    print(dept[1] == dept[4])

    emp = sorted(dept, reverse=True)
    print(emp)


if __name__ == "__main__":
    main()