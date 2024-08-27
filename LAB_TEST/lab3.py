while True:
 print("<<Point a>>")
 x1 = int(input("Enter x coordinate: "))    
 y1 = int(input("Enter y coordinate: "))
 print("<<Point b>>")
 x2 = int(input("Enter x coordinate: "))    
 y2 = int(input("Enter y coordinate: "))

 result = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
 horizontal = abs(x1 - x2)
 Vertical = abs(y1 - y2)
 if x1 == x2 and y1 == y2:
        direction = "nowhere"
 elif x1 == x2:
        direction = "north" if y1 < y2 else "south"
 elif y1 == y2:
        direction = "east" if x1 < y2 else "west"
 else:
        if x1 < x2 and y1 < y2:
            direction = "north-east"
        elif x1 < x2 and y1 > y2:
            direction = "south-east"
        elif x1 > x2 and y1 < y2:
            direction = "north-west"
        elif x1 > x2 and y1 > y2:
            direction = "south-west"
 if (x1, y1) == (0, 0) and (x2, y2) == (0, 0):
            print("Goodbye")
            break

 print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}):")
 print(f"Euclidean distance is {result:.2f}.")
 print(f"Horizontal distance is {horizontal}.")
 print(f"Vertical distance is {Vertical}.")
 print(f"We are going {direction}.")
