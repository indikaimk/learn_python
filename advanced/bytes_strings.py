
def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "ABCD"
    print(s)

    #combining bytes and strigs
    #print(s+b) => this does not work

    #decode and combine
    s2 = b.decode('utf-8')
    print(s+s2)

    #encoding a string
    b2 = s.encode('utf-8')
    print(b+b2)

    #encode with utf-32
    b3 = s.encode('utf-32')
    print(b3)


if __name__ == "__main__":
    main()