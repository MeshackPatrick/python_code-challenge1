def convert_hours(hour, minute, meridian):
    if meridian == "am":
        if hour == 12:
            hour = 0
    elif meridian == "pm":
        if hour != 12:
            hour += 12

    return f"{hour:02d}{minute:02d}"


print(convert_hours(8, 30, "am"))
print(convert_hours(8, 30, "pm"))
