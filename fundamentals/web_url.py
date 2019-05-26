import urllib.request as request

def main():
  web_url = request.urlopen("http://google.lk")
  print("result code: " + str(web_url.getcode()))

if __name__ == "__main__":
  main()