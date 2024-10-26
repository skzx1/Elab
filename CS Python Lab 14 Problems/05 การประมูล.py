'''การประมูล
ให้นิสิตเขียนโปรแกรมเพื่อเก็บข้อมูลการประมูลสินค้า โดยจะมีการใส่ชื่อเว้นวรรคราคาประมูลซึ่ง 1 คนสามารถประมูลได้หลายครั้ง จนกว่าผู้ใช้จะใส่คำว่า end หลังจากนั้นให้แสดงชื่อผู้ประมูล ราคาประมูลสูงสุดและจำนวนครั้งในการประมูลของคนนั้นๆ เรียงตามลำดับตัวอักษรของชื่อผู้ประมูล และสรุปผลการประมูลว่าใครเป็นผู้ชนะการประมูล ถ้าประมูลราคาเท่ากันให้ผู้ที่ประมูลก่อนชนะ
ตัวอย่าง
ข้อมูลเข้า	ข้อมูลออก
kong 100
saac 500
kong 300
pp 1000
saac 900
end
kong bid at the price of 300.0 baht in 2 times.
pp bid at the price of 1000.0 baht in 1 time.
saac bid at the price of 900.0 baht in 2 times.
The winner is pp.
'''
name_count = {}
name_price = {}
bid = []
while True:
    list_name = input().split()
    if list_name[0] == 'end':
        break
    if len(list_name) < 2:
        continue
    
    name = list_name[0]
    price = float(list_name[1])
    bid.append((name, price))
    
    if name in name_count:
            name_count[name] += 1
            if price > name_price[name]:
                name_price[name] = price
    else:
        name_count[name] = 1
        name_price[name] = price

sorted_names = []
for name in name_count:
    sorted_names.append(name)
sorted_names.sort()

for name in sorted_names:
    if name_count[name] == 1:
        print(f"{name} bid at the price of {name_price[name]:.1f} baht {name_count[name]} time")
    else:
        print(f"{name} bid at the price of {name_price[name]:.1f} baht {name_count[name]} times.")

max_price = 0
winner = ''

for name, price in bid:
    if price > max_price:
        max_price = price
        winner = name
    elif price == max_price and winner == '':
        winner = name
print(f"The winner is {winner}.")