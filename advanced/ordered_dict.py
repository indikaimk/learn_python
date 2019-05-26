from collections import OrderedDict

def main():
    #A list of sport teams with wins and loses
    sportTeams = [("Rovals", (10, 12)), ("Dragons", (20, 12)), ("Cats", (3, 12)), ("Blakes", (31, 10)),
                    ("Rockets", (10, 9))]

    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    teams = OrderedDict(sortedTeams)
    print(teams)

    #using popitem() to remove the top item
    tm, wl = teams.popitem(False)
    print("Top team:", tm, wl)

    #iterate top 4 items
    for i, team in enumerate(teams, start=1):
        print(1, team)
        if i == 4:
            break
    
    #test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    c = {"a": 1, "c": 3, "b": 2}
    print("Equality test: ", a == b)
    print("Equality test: ", a == c)


if __name__ == "__main__":
    main()