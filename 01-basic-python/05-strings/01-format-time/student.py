def format_time(hours, minutes, seconds):
    list = [hours, minutes, seconds]
    for i in list:
        if len(str(i)) == 1 and i == hours:
            hours = f"{0}{hours}"
        if len(str(i)) == 1 and i == minutes:
            minutes = f"{0}{minutes}"
        if len(str(i)) == 1 and i == seconds:
            seconds = f"{0}{seconds}"
    return "{}:{}:{}".format(hours, minutes, seconds)
