from datetime import date
from datetime import time
from datetime import datetime

def main():
  today = date.today()
  print("Today's date", today)

  print("Date components", today.day, today.month, today.year)
  print("Today's weekday # is", today.weekday())
  days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
  print("which is a:", days[today.weekday()])
  now = datetime.now()
  print("The current date and time is", now)
  t = datetime.time(now)
  print("Time is", t)


if __name__ == "__main__":
  main()

