def main():
    ctemps = [10, 20, 24, 32, 80]

    #dictionary comprehension
    tempDict = {t: (t*9/5 + 32) for t in ctemps if t < 80}
    print(tempDict)
    print(tempDict[20])

    #merge dictionaries
    team1 = {"John": 24, "Bob": 10, "Smith": 11, "Tom": 30}
    team2 = {"Jack": 9, "Jim": 14, "Tim": 15}
    newTeam = {k:v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)

if __name__ == "__main__":
    main()