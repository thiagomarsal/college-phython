# IT 280 – Lab #3: Selection of Mathematical Functions Instructions

# Calculate the area of a circle given the diameter of the circle.
def areacircle(radius):
    return 3.14159 * (radius * radius)


# Calculate the area of a square.
def areasquare(side):
    return side * side


# Calculate the area of a triangle.
def areatriangle(base, height):
    return height * base / 2


# Calculate the MPG for a vehicle, when provided the distance traveled and the amount of fuel used.
def mpg(miles, gallons):
    return miles / gallons


# Calculate the total number of hours worked in a week, when provided the hours worked each day of the week.
def totalhour(hours):
    return sum(hours)


def main():
    # Control variable to quit the program/loop
    option = ''
    while option != '0':
        # Print the menu
        print()
        print('Menu:')
        print('\t1. Calculate Area of a Circle')
        print('\t2. Calculate Area of a Square')
        print('\t3. Calculate Area of a Triangle')
        print('\t4. Calculate MPG for a vehicle')
        print('\t5. Calculate Total Hour Worked in a Week')
        print('\t0. Exit')
        option = input('Option: ')

        result = ''
        if option == '1':
            value = int(input('Please, inform the radius or diameter of a circle: '))
            result = areacircle(value)
        elif option == '2':
            value = int(input('Please, inform the side of a square: '))
            result = areasquare(value)
        elif option == '3':
            value1 = int(input('Please, inform the base of a triangle: '))
            value2 = int(input('Please, inform the height of a triangle: '))
            result = areatriangle(value1, value2)
        elif option == '4':
            value1 = int(input('Please, inform how many miles you drove: '))
            value2 = int(input('Please, inform how many gallons to refill the tank: '))
            result = mpg(value1, value2)
        elif option == '5':
            values = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
            listHours = []
            for i in range(7):
                listHours.append(int(input('Please, inform how many hours you worked on ' + values.get(i) + ': ')))
            result = totalhour(listHours)

        print('The operation result is: ' + str(result))

main()