'''ดอกเบี้ย
จงเขียนโปรแกรมเพื่อรับค่าเงินต้น (principle) ในหน่วยบาท อัตราดอกเบี้ย (interest rate) ในหน่วยร้อยละต่อปี และระยะเวลากู้ยืม (time) ในหน่วยปี แล้วสร้างและเรียกใช้ฟังก์ชันเพื่อคำนวนหาจำนวนเงินรวมที่ต้องจ่ายเมื่อครบระยะเวลากู้ยืมใน 2 รูปแบบ ดังนี้

simple_interest(p, r, t) เพื่อคืนค่าเงินรวมของการคิดดอกเบี้ยเชิงเดี่ยว จากสูตร
ดอกเบี้ย = เงินต้น x อัตราดอกเบี้ย x ระยะเวลากู้ยืม

compound_interest(p, r, t) เพื่อคืนค่าเงินรวมของการคิดดอกเบี้ยทบต้น จากสูตร
เงินรวม = เงินต้น x (1 +อัตราดอกเบี้ย) ระยะเวลากู้ยืม

ตัวอย่าง Input/Output
Enter principle: 25000
Enter interest rate: 3.25
Enter time: 6.5
Return money for simple interest calculation is 30281.25 Baht.
Return money for compound interest calculation is 30776.94 Baht.

'''
def simple_interest(p, r, t):
    r /= 100
    dok = p * r * t + p
    return dok
def compound_interest(p, r, t):
    r /= 100
    dok = p * (1 + r)**t 
    return dok

p = float(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))
print('Return money for simple interest calculation is {:.2f} Baht.'.format(simple_interest(p, r, t)))
print('Return money for compound interest calculation is {:.2f} Baht.'.format(compound_interest(p, r, t)))