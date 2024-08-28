'''มาตรการเงินโอน แก้จน คนขยัน
Negative Income Tax หรือ NIT เป็นแนวทางหนึ่งที่นักวิชาการเสนอเพื่อลดความเหลื่อมล้ำในการกระจายรายได้ ที่มักเป็นปัญหาที่แต่ละประเทศต้องประสบเมื่อเศรษฐกิจโตขึ้น โดยแทนที่รัฐบาลจะเก็บภาษีจากประชาชน NIT จะเป็นการให้เงินกับประชาชน NIT จัดเป็นการช่วยเหลือคนจนของรัฐบาลในรูปแบบของการโอนเงินให้แก่บุคคลที่มีรายได้ต่ำกว่าเกณฑ์ โดยใช้การวัดระดับรายได้เป็นเครื่องมือในการระบุผู้ที่ควรจะได้รับสิทธิ สำนักงานเศรษฐกิจการคลังได้เสนอแนวทางการดำเนินการเบื้องต้น ดังนี้

ผู้รับสิทธิ NIT ต้องเป็นคนไทยอายุตั้งแต่ 15-60 ปี ที่กําลังทํางานอยู่ โดยไม่กําหนดสายอาชีพ และมีรายได้สุทธิ (net income) ตั้งแต่ 1 – 79,999 บาทต่อปี
โดยรายได้ตั้งแต่ 1 – 30,000 บาทต่อปี จะได้เงินโอนภาษีจากรัฐ 20% ของรายได้สุทธิ แต่หากรายได้มากกว่า 30,000 บาทต่อปีขึ้นไป ก็จะได้รับโอนเงินภาษีลดลง 12% ของส่วนที่เกิน 30,000 บาท ไปจนถึงรายได้ 79,999 บาท
ส่วนที่มีรายได้ 80,000 บาทขึ้นไป จะไม่ได้รับเงินโอนภาษีจากรัฐ เพราะถือว่ามีรายได้ที่มากพอแล้ว เทียบเคียงกับการได้รับค่าแรงขั้นต่ำ 300 บาทต่อวัน
จงเขียนโปรแกรมเพื่อรับอายุ และรายได้สุทธิของคนไทย เพื่อสร้างและเรียกใช้ฟังก์ชันเพื่อคำนวนหาจำนวนเงินที่รัฐจะต้องจ่ายคืนให้ตามมาตรการ NIT ข้างต้น

หมายเหตุ ให้แสดงข้อความ "Invalid age." หรือ "Invalid income." เมื่ออายุหรือเงินได้สุทธิไม่ถูกต้อง หรือไม่อยู่ในช่วงที่จะมีสิทธิได้รับ NIT

ที่มาข้อมูล:

http://www.moneyandbanking.co.th/analysis.php?isb=isb007&newsID=8199 เข้าถึงเมื่อ 21 ก.ย. 2557
http://www.naewna.com/business/115996 เข้าถึงเมื่อ 21 ก.ย. 2557
ตัวอย่าง Input/Output 1
Enter your age: 34
Enter your net income: 28500
Your negative income tax is 5700.00 Baht.
ตัวอย่าง Input/Output 2
Enter your age: 42
Enter your net income: 79999
Your negative income tax is 0.12 Baht.
ตัวอย่าง Input/Output 3
Enter your age: 54
Enter your net income: 35000
Your negative income tax is 5400.00 Baht.
ตัวอย่าง Input/Output 4
Enter your age: 44
Enter your net income: 30050
Your negative income tax is 5994.00 Baht.
ตัวอย่าง Input/Output 5
Enter your age: 12
Enter your net income: 80000
Invalid age.'''
age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
if age < 15 or age > 60:
    print("Invalid age.")
elif income <= 0 or income >= 80000  :
    print("Invalid income.")
else :
    if 1 < income <= 30000 :
        x = income * 20 / 100
        print(f"Your negative income tax is {x:.2f} Baht.")
    elif income > 30000:
        y = (6000 - 0.12 * (income - 30000))
        print(f"Your negative income tax is {y:.2f} Baht.")
