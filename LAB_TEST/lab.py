day = int(input(""))
hours = int(input(""))
minutes = int(input(""))
y = ""
if (hours == 4 and minutes >= 1) or (hours > 4 and hours < 12) or (hours == 12 and minutes == 0):
    y = "good-morning"
elif (hours == 12 and minutes >= 1) or (hours > 12 and hours < 18) or (hours == 18 and minutes == 0):
    y = "good-afternoon"
elif (hours == 18 and minutes >= 1) or (hours > 18 and hours < 22) or (hours == 22 and minutes == 0):
    y = "good-evening"
else:
    y = "good-night"
    
x = ""
if day == 1:
    x = "sunday.png"
elif day == 2:
    x = "monday.png"
elif day == 3:
    x = "tuesday.png"
elif day == 4:
    x = "wednesday.png"
elif day == 5:
    x = "thursday.png"
elif day == 6:
    x = "friday.png"
elif day == 7:
    x = "saturday.png"

print(f"{y}-{x}")

