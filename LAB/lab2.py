print("Upper left corner coordinate:")
x1 = int(input("  << x axis: "))
y1 = int(input("  << y axis: "))
Eastern = int(input("  << Eastern: "))
Southern = int(input("  << Southern: "))

print("Enter a coordinate:")
x2 = int(input("  << x axis: "))
y2 = int(input("  << y axis: "))

rec = x1 + Eastern
rec2 = y1 - Southern

if x1 <= x2 <= rec and rec2 <= y2 <= y1:
    print(f">>> ({x2:.2f}, {y2:.2f}) is inside the rectangle.")
else:
    print(f">>> ({x2:.2f}, {y2:.2f}) is not inside the rectangle.")











