'''ระยะเวลา
จงเขียนโปรแกรมเพื่อรับค่าเวลาเริ่มต้น (start time) และเวลาสิ้นสุด (finish time) ซึ่งกำหนดให้เวลาของวันเดียวกันเพื่อคำนวณหาระยะเวลาระหว่างเวลาทั้งสอง โดยกำหนดให้สร้างฟังก์ชันต่อไปนี้

read_hour() เพื่อคืนค่าชั่วโมงในระบบ 24 ชั่วโมง (นั่นคือ ค่าที่เป็นไปได้มีค่าตั้งแต่ 0 ถึง 23)
read_minute() เพื่อคืนค่านาที (ค่าที่เป็นไปได้มีค่าตั้งแต่ 0 ถึง 59)
read_second() เพื่อคืนค่าวินาที (ค่าที่เป็นไปได้มีค่าตั้งแต่ 0 ถึง 59)
to_seconds(h, m, s) เพื่อคืนค่าจำนวนวินาทีทั้งหมดของเวลา h ชั่วโมง m นาที และ s วินาที
time_elapsed(start, finish) เพื่อคืนค่าระยะเวลานับจากวินาทีที่ start ถึงวินาทีที่ finish
แนะนำ ถ้าเวลาเริ่มต้นและเวลาสิ้นสุดมีค่าเป็น 8:15:00 ถึง 13:20:00 ตามลำดับ ในการหาระยะเวลาระหว่างเวลาทั้งสอง เราสามารถทำได้โดยแปลงเวลาทั้งสองให้อยู่ในรูปของจำนวนวินาทีนับจากเวลา 00:00:00 แล้วหาผลต่างของค่าทั้งสอง

ตัวอย่าง Input/Output
Start time:
>> Enter hour: 8
>> Enter minute: 15
>> Enter second: 0
Finish time:
>> Enter hour: 13
>> Enter minute: 20
>> Enter second: 0
Elapsed time is 5 hours 5 minutes 0 seconds.'''
def read_hour():
    h = int(input("Enter hour: "))
    return h
def read_minute(): 
    m = int(input("Enter minute: "))
    return m
def read_second():
    s = int(input("Enter second: "))
    return s
def to_seconds(h, m, s):
    Sec = h * 3600 + m * 60 + s
    return Sec
def time_elapsed(start, finish):
    elapsed = finish - start
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60
    return f"{hours} hours {minutes} minutes {seconds} seconds."
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))