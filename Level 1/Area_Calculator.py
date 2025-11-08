
isRunning = True
while isRunning:
 print("Welcome to the Area Calculator!")
 print("Select the shape you would like to calculate the area for:")
 print("1. Rectangle")
 print("2. Circle")
 print("3. Triangle")
 print("4. Square")
 print("5. Exit")
 choice = int(input("Enter the number of your choice (1-5): "))
 if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers.")
        else:
            area = length * width
            print(f"The area of the rectangle is {area} square units.")
            
        
 elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        if radius <= 0:
            print("Radius must be a positive number.")
        else:
            area = 3.14159 * radius**2
            print(f"The area of the circle is {area} square units.")

 elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        if base <= 0 or height <= 0:
            print("Base and height must be positive numbers.")
        else:
            area = 0.5 * base * height
            print(f"The area of the triangle is {area} square units.")
        
 elif choice == 4:
        side = float(input("Enter the side length of the square: "))
        if side <= 0:
            print("Side length must be a positive number.")
        else:
            area = side**2
            print(f"The area of the square is {area} square units.")
        
 elif choice == 5:
        print("Exiting the program.")
        isRunning = False
 else:
        print("Invalid choice. Please select a number between 1 and 5.")
        choice = int(input("Enter the number of your choice (1-5): "))