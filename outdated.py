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
        date_string = input("Date: ").strip()

        date_components = re.split(r"[\/,\-\s]+", date_string)

        date_tuple = check_date_and_return(date_components)
        if date_tuple:
            break

    print(f"{date_tuple[0]}-{date_tuple[1]:02}-{date_tuple[2]:02}")


def check_date_and_return(date_components):
    # this function checks the date components and returns them in the correct format, or returns False if one of the checks fail

    try:
        month, day, year = date_components

        year = int(year)

        if month.title() in months:
            month = months.index(month.title()) + 1
        else:
            month = int(month)
            if month < 1 or month > 12:
                raise ValueError

        day = int(day)
        if day < 1 or day > 31:
            raise ValueError

    except ValueError:
        return None

    return year, month, day


main()
