# Author: ATN 10/12/21

x_coord_first = int(input("Enter your first x coordinate: "))
y_coord_first = int(input("Enter your first y coordinate: "))

x_coord_second = int(input("Enter your second x coordinate: "))
y_coord_second = int(input("Enter your second y coordinate: "))

distance_formula = (((x_coord_second - x_coord_first) ** 2) + ((y_coord_second - y_coord_first) ** 2) ** (1/2))

print("The distance is " + str(distance_formula))
