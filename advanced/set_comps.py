def main():
    ctemps = [5, 10, 15, 20, 34, 20, 40, 19, 4, 24, 20]
    ftemps1 = [t*9/5 + 32 for t in ctemps]
    ftemps2 = {t*9/5 + 32 for t in ctemps}
    print(ftemps1)
    print(ftemps2)

    #build a set of Farenhite temperatures

    #build a set from an input source
    sTemp = "The quick brown fox"
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)


if __name__ == "__main__":
    main()
