data = []
max_position = 0
while True:
    text = input().strip()
    if text == '-1':
        break
    data.append(text)
for i in data:
    position = i.find('=')
    if position != -1:
        side1 = i[:position].strip()
        max_position = max(max_position, len(side1))
for i in data: 
    position = i.find('=')
    if position == -1:
        print(i)
    else:
        side1 = i[:position].strip()
        side2 = i[position+1:].strip()
        space = max_position - len(side1)
        print(f"{' ' * space}{side1} = {side2}")
        