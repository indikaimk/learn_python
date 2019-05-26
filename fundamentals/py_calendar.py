import calendar

def main():
  c = calendar.TextCalendar(calendar.MONDAY)
  st = c.formatmonth(2019, 1, 1)
  print(st)

  hc = calendar.HTMLCalendar(calendar.MONDAY)
  ht = hc.formatmonth(2019, 1, 1)
  print(ht)

  for i in c.itermonthdays(2019, 1):
    print(i)
  
  for name in calendar.month_name:
    print(name)

  for day in calendar.day_name:
    print(day)

  print("Team meetings will be on:")
  for m in range(1, 13):
    cal = calendar.monthcalendar(2019, m)
    week1 = cal[0]
    week2 = cal[1]
    if week1[calendar.FRIDAY] != 0:
      meetday = week1[calendar.FRIDAY]
    else:
      meetday = week2[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))


if __name__ == "__main__":
  main()