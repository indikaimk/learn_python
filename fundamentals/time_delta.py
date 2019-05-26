from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
  print(timedelta(days=365, hours=5, minutes=1))
  now = datetime.now()
  print("Today is", str(now))
  print("one year from now will be", str(now + timedelta(days=365)))
  print("2 days and 3 weeks from now will be", str(now + timedelta(days=2, weeks=3)))

  t = now - timedelta(weeks=1)
  s = t.strftime("%A %B %d, %y")
  print("1 week ago it was:", s)

  today = date.today()
  #today = date(2019, 5, 30)
  afd = date(today.year, 4, 1)
  if afd < today:
    print("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year+1)
  time_to_afd = afd - today
  print("It is just", time_to_afd.days, "days untill April Fool's day")

if __name__ == "__main__":
  main()