time = input().split()
hour = int(time[0])
minute = int(time[1])

if minute >= 45:
    minute = minute - 45
else:
    mid = 45 - minute
    minute = 60 - mid
    if hour != 0:
        hour -= 1
    else:
        hour = 23

print(hour, minute)


