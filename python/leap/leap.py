def is_leap_year(year):
    # TRUE: on every year that is evenly divisible by 4
    if year % 4 == 0:
        # FALSE: except every year that is evenly divisible by 100
        if year % 100 == 0:
            # TRUE: unless the year is also evenly divisible by 400
            if year % 400 == 0:
                return True
            return False
        return True
    return False
