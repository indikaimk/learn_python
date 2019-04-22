import os 
from os import path
import datetime
from datetime import date, timedelta
import time

def main():
  print(os.name)
  print("item exists: " + str(path.exists("text_file.txt")))
  print("item is a file: " + str(path.isfile("text_file.txt")))
  print("item is a directory: " + str(path.isdir("text_file.txt")))

  print("item path: ", str(path.realpath("text_file.txt")))
  print("item path and name: ", str(path.split(path.realpath("text_file.txt"))))

  t = time.ctime(path.getmtime("text_file.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("text_file.txt")))

  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("text_file.txt"))
  print("It has been " + str(td) + " since the file was modified.")
  print("The file was modified " + str(td.total_seconds()) + " ago")

if __name__ == "__main__":
  main()