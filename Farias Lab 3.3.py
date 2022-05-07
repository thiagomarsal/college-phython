# IT 280 – Lab #4: List Manipulation Lab Instructions

# Sort list
def sort(list):
    list.sort(key=int)


# Remove duplicates
def removeDuplicate(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist


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

    sort(list)
    list = removeDuplicate(list)
    print('Here you are your unique ordered list: ' + str(list))


main()
