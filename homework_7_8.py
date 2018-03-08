# 7
date = '05.17.2016'
month = int(date[:2])
day = int(date[3:5])
year = int(date[6:])
date = ("American date: %d. %d. %d." % (month, day, year))
date1 = ("European date: %d. %d. %d. " % (day, month, year))
print(date)
print(date1)

# 8
name = 'Aleksey Yudin'
lst = name.split()
print(lst[0], lst[1], '->', lst[1], lst[0])
