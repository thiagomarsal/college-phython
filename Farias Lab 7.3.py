# IT 280 – Lab #13: Time and Date Instructions
import datetime


def askTime(text):
    while True:
        try:
            print('Please, a date in YYYY-MM-DD format', text, end=': ')
            date = input()
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            break
        except:
            print('ERROR - Date must be informed in a proper format "YYYY-MM-DD"')

    if text.__contains__('Wright Brothers') and date.year < 1908:
        print('\tThis information is inaccurate. The Wright Brothers did not make a public flight until 1908,\n'
              '\ttwo years after the Brazilian Santos Dumont who flew in November 12, 1906.')

    return date


def printTimeLapse(start, end):
    duration = end - start
    days = divmod(duration.total_seconds(), 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    seconds = divmod(minutes[1], 1)
    print("Time between dates is: %d days, %d hours, %d minutes and %d seconds." % (days[0], hours[0], minutes[0], seconds[0]))


def main():
    napoleao = askTime('The birthdate of Napoleon Bonaparte')
    printTimeLapse(napoleao, datetime.datetime.now())

    pearHarbor = askTime('The bombing of Pearl Harbor')
    printTimeLapse(pearHarbor, datetime.datetime.now())

    wrightBrothers = askTime('The Wright Brothers 1st flight')
    printTimeLapse(wrightBrothers, datetime.datetime.now())


main()
