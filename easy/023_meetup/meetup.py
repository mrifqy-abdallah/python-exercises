from datetime import date
from calendar import monthcalendar, setfirstweekday


class MeetupDayException(Exception):
    """ Return exception when encountered """
    def __init__(message):
        super().__init__("No such date exists")

        
def meetup(year:int, month:int, week:str, day_of_week:str):
    setfirstweekday(6)  # Set Sunday as the first day of the week 
    weeks = {
        "1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5, "teenth": 3, "last": 5
    }
    days = {
        "sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6
    }

    month_calendar = monthcalendar(year, month)  # Return a list of the month's calendar
    day = days[day_of_week.lower()]
    the_week = weeks[week]
    the_date = 0
    count = 0

    for each_week in month_calendar:
        if each_week[day] != 0:
            the_date = each_week[day]
            count += 1
        if count == the_week:
            break
    
    # This one case needs to be re-counted
    if week == "teenth" and the_date >= 20:
        the_date -= 7

    try:
        if count != the_week and week != "last":  # 'last' category is excluded from the exception
            raise MeetupDayException()
    except Exception:
        raise
        
    return date(year, month, the_date)
