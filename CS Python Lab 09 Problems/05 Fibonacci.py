'''Fibonacci
ในทางคณิตศาสตร์ เลขฟีโบนัชชี (อังกฤษ: Fibonacci number) เป็นเลขในลำดับเลขฟีโบนัชชี จำกัดความหมายด้วยสูตร:

F
n
:=
F
(
n
)
:=
⎧
⎨
⎩
1
, 
n
=
1
1
, 
n
=
2
F
(
n
−
1
)
+
F
(
n
−
2
)
, 
n
>
2
โดยกฎว่าเลขลำดับแรกคือ 1 ลำดับที่สองคือ 1 และลำดับถัดไปคือผลบวกของเลขในสองลำดับก่อนหน้านี้ รายชื่อตัวเลขดังนี้คือลำดับเลขฟีโบนัชชี เริ่มต้นจากลำดับแรก:

1
,
1
,
2
,
3
,
5
,
8
,
13
,
…
ชื่อของจำนวนฟีโบนัชชีตั้งขึ้นเพื่อเป็นเกียรติแก่นักคณิตศาสตร์ชาวอิตาลีชื่อ ลีโอนาโดแห่งปิซา (Leonardo de Pisa) ซึ่งเป็นที่รู้จักกันในนามฟีโบนัชชี (Fibonacci) ผู้ค้นพบลำดับฟีโบนัชชีในต้นศตวรรษที่ 13

เขียนโปรแกรมเพื่อหาค่าฟิโบนัชชีในลำดับที่ n เมื่อ n เป็นจำนวนเต็มบวก

หมายเหตุ ถ้าใช้วิธีการแบบ recursive จะไม่ผ่าน 2 cases สุดท้าย เพราะเวลาที่ใช้จะมากเกินกว่าเวลาที่ยอมรับได้

ตัวอย่างโปรแกรม 1
Enter n: 5
fibo(5) = 5
ตัวอย่างโปรแกรม 2
Enter n: 8
fibo(8) = 21'''
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    num = 1
    num1 = 1
    i = 3
    while i <= n:
        re = num + num1
        num = num1
        num1 = re
        i += 1
    return num1
n = int(input("Enter n: "))
print("fibo({}) = {}".format (n, Fibonacci(n)))