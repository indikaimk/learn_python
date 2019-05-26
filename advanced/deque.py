#double ended queue
import collections
import string

def main():
    d = collections.deque(string.ascii_lowercase)
    print(d)
    print("Item count: ", str(len(d)))

    #iterate
    for e in d:
        print(e.upper(), end=",")

    #manipulate itmes
    print(d.pop())
    d.popleft()
    d.append(1)
    d.appendleft(2)
    print(d)

    #rotate items
    d.rotate(10)
    print(d)

if __name__ == "__main__":
    main()