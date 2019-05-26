def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    #use iter() to create an interator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    
    #iterate using a function
    with open("advanced/test.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    #use regular iteration
    # for d in range(len(days)):
    #     print(d+1, days[d])
    
    #using enumrate
    for i, m in enumerate(days, start=1):
        print(i, m)

    #iterating over combine sequences
    # for m in zip(days, months):
    #     print(m)

    for i, m in enumerate(zip(days, months), start=1):
        print(i, m[0], m[1])


if __name__ == "__main__":
    main()