import datetime

start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
days = (end - start).days
curr = start
aday = datetime.timedelta(days=1)
count = 0
for i in range(days + 1):
    if curr.weekday() == 6 and curr.day == 1:
        count += 1
    curr += aday
print count
