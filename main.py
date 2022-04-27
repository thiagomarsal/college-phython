# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

age = 30
name = 'Larry'

if name == 'Sam':
    print ('Hi, Sam')
elif age < 30:
    print ('Hi, Sally')
elif age > 30:
    print ('Hi, Gary')
else:
    print ('Hi, David')

spam = 0

while spam < 5:
    print ('Hello World ' + str(spam))
    spam = spam + 1