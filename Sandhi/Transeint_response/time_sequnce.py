"""def yield_times():
    from datetime import date, time, datetime, timedelta
    start = datetime.combine(date.today(), time(0, 0))
    yield start.strftime("%S")
    while True:
        start += timedelta(seconds=7)
        yield start.strftime("%S")
gen = yield_times()
for ii in range(5):
    print gen.next()"""
    
"""stack = [1,2,3,4,5,6,7,8,9]
ans = []
for i in range(0,5):
    ans.append(stack.pop(i))
    print("Ans",ans)"""
    
first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]
third = []

a = len(first)
b = int(0)
while True:
    x = first[b]
    y = second[b]
    ans = x + y
    third.append(ans)
    b = b + 1
    if b == a:
        break

print third
    