def add_time(time1, time2, start_day=''):
    day_of_week_index = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5,
                         'Sunday': 6}
    # split time1 (start time) into hour and minute
    hr1 = time1.split(':')[0]
    m1 = time1.split(':')[1].split()[0]
    am_or_pm = time1.split()[1]
    # print(hr1, m1)
    # convert to 24 hour format
    if am_or_pm == "PM":
        hr1 = int(hr1) + 12
    # split time2 (duration) into hour and minute
    hr2 = time2.split(':')[0]
    m2 = time2.split(':')[1]
    # print(hr2, m2)

    # Calculate total hours and minutes
    mn_total = int(m1) + int(m2)
    minutes = mn_total % 60
    extra_hrs = mn_total // 60
    hr_total = int(hr1) + int(hr2) + extra_hrs

    # final hours as 12 hour format
    hours = (hr_total % 24) % 12
    # handle midday and midnight
    if hours == 0:
        hours = 12
    hours = str(hours)

    # calculate number of days
    n_days = (hr_total // 24)

    # decide AM or PM
    ending = ""
    if (hr_total % 24) < 12:
        ending = "AM"
    else:
        ending = "PM"
    # concatenate 0 before single digit minutes (minutes from 0 to 9)
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)

    # return new time
    new_time = hours + ":" + minutes + " " + ending

    if start_day == '':
        if n_days == 0:
            return new_time
        if n_days == 1:
            return new_time + ' (next day)'
        return new_time + ' (' + str(n_days) + ' days later)'
    else:
        day = (day_of_week_index[start_day.lower().capitalize()] + n_days) % 7
        for k, v in day_of_week_index.items():
            if v == day:
                day = k
                break
        if n_days == 0:
            return new_time + ', ' + day
        if n_days == 1:
            return new_time + ', ' + day + ' (next day)'
        return new_time + ', ' + day + ' (' + str(n_days) + ' days later)'
