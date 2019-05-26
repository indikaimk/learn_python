def main():
  #f = open("text_file.txt", "w+")
  #f = open("text_file.txt", "w")
  #f = open("text_file.txt", "a")
  f = open("text_file.txt", "r")
  # for i in range(10):
  #   #f.write("this is line " + str(i) + " \r\n")
  #f.close
  # if f.mode == 'r':
  #   contents = f.read()
  #   print(contents)

  if f.mode == "r":
    fl = f.readlines()
    for x in fl:
      print(x, end='')

if __name__ == "__main__":
  main()