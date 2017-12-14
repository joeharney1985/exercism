import datetime

weekday_map = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}

n_week_map = {
    '1st': 0,
    '2nd': 1,
    '3rd': 2,
    '4th': 3,
    '5th': 4,
    'last': -1,
}


def all_days_that_match_dow(year, month, day_of_the_week):
    first_of_month = datetime.date(year=year, month=month, day=1)
    first_of_month_dow = first_of_month.weekday()

    dow = weekday_map[day_of_the_week.lower()]
    day_diff = dow - first_of_month_dow
    if day_diff < 0:
        day_diff += 7

    foo = first_of_month + datetime.timedelta(days=day_diff)
    out = []
    while foo.month == month:
        out.append(foo)
        foo += datetime.timedelta(days=7)
    return out


def meetup_day(year, month, day_of_the_week, which):
    which = which.lower()
    all__days_in_month = all_days_that_match_dow(year, month, day_of_the_week)

    if which in n_week_map:
        return all__days_in_month[n_week_map[which]]
    if which == 'teenth':
        for d in all__days_in_month:
            if d.day >= 13:
                return d
