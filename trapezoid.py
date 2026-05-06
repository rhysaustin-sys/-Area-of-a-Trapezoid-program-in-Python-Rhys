#area of a Trapezoid 
#This program calculates the area of a trapezoid given the lengths of the two parallel sides and the height.
#Get the lengths of the two parallel sides and the height from the user
base_a = int(input("Enter the length of the first parallel side (base A): "))
base_b = int(input("Enter the length of the second parallel side (base B): "))
height = int(input("Enter the height of the trapezoid: "))

#Calculate the area of the trapezoid using the formula: Area = (base_a + base_b) * height / 2
area = (base_a + base_b) * height / 2
#Display the result
print("The area of the trapezoid is:", area)