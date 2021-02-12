side_a = float(input("Please enter A: "))
side_b = float(input("Please enter B: "))
side_c = float(input("Please enter C: "))

side_a, side_b, side_c = input("Please enter 3 sides of triangle: ").split()
half_perimeter = (float(side_a) + float(side_b) + float(side_c)) / 2
triangel_square = (half_perimeter * (half_perimeter - float(side_a)) * (half_perimeter - float(side_b)) * (half_perimeter - float(side_c))) ** 0.5
print(triangel_square)


#просто название
half_perimeter = (side_a + side_b + side_c) / 2
triangel_square = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5
print(triangel_square)
