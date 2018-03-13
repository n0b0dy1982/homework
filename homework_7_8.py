# 7
date = '05.17.2016'
month = int(date[:2])
day = int(date[3:5])
year = int(date[6:])
date1 = ("American date: %d. %d. %d" % (month, day, year))
date2 = ("European date: %d. %d. %d" % (day, month, year))
print(date1)
print(date2)

# 8
name = 'Aleksey Yudin'
lst = name.split()
print(lst[0], lst[1], '->', lst[1], lst[0])
