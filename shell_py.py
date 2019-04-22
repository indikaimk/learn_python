import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  if path.exists("textfile.txt"):
    src = path.realpath("text_file.txt")
    dst = src + ".bak"
    #shutil.copy(src, dst)
    #shutil.copystat(src, dst)

    #os.rename("text_file.txt", "textfile.txt")
    #root_dir, tail = path.split(src)
    #shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("testzip.zip", "w") as newzip:
      newzip.write("textfile.txt")
      newzip.write("text_file.txt.bak")

if __name__ == "__main__":
  main()