# IT 280 – Lab #6: IT 280 – Lab #6: Package Creation Lab Instructions

import util


def main():
    # Control variable to quit the program/loop
    option = ''
    list = []
    while option != '0':
        # Print the menu
        print()
        print('Menu:')
        print('\t1. Add a number')
        print('\t0. Exit')
        option = input('Option: ')
        print()

        if option == '1':
            value = int(input('Please, inform a number: '))
            list.append(value)
            for i in range(len(list)):
                print('Index: ' + str(i) + ', Value: ' + str(list[i]))
        elif len(list) == 0 and option == '0':
            print('\nEmpty list is not allowed. Please, inform at least one value.')
            option = ''

    util.sortHigh(list)
    list = util.removeDuplicate(list)
    print('Here you are your unique ordered listed high: ' + str(list))

    util.sortLow(list)
    print('Here you are your unique ordered listed low: ' + str(list))


main()
