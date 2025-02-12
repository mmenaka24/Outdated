import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():

    while True:
        date_string = input("Date: ")

        date_components = re.split(r"[\/,\-\s]+", date_string)

        to_print = check_date_and_return(date_components)
        if not to_print == False:
            break

    print(f"{to_print[0]}-{to_print[1]:02}-{to_print[2]:02}")


def check_date_and_return(date_components):
    # this function checks the date components and returns them in the correct format, or returns False if one of the checks fail

    try:
        month, day, year = date_components
    except ValueError:
        return False

    try:
        year = int(year)
        if year < 0:
            raise ValueError
    except ValueError:
        return False

    month = month.title()

    if month in months:
        month = months.index(month) + 1
    else:
        try:
            month = int(month)
            if month < 1 or month > 12:
                raise ValueError
        except ValueError:
            return False

    try:
        day = int(day)
        if day < 0 or day > 31:
            raise ValueError
    except ValueError:
        return False

    return year, month, day


main()
