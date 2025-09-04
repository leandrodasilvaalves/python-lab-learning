from datetime import date, datetime, timedelta

now = datetime.now()


print(now)
print(now.year)
print(now.strftime("%A"))
print(now.strftime("%a"))
print(now.strftime("%B"))
print(now.strftime("%b"))
print(now.strftime("%w"))
print(now.strftime("%W"))

print(now.strftime("%H"))
print(now.strftime("%M"))
print(now.strftime("%S"))
print(now.strftime("%f"))


def print_interval(begin, interval, end):
    print("".rjust(50, "."))
    print(f"begin: {begin}")
    print(f"interval {interval}")
    print(f"end: {end}")


start_day = date.today()
interval = timedelta(days=60)
end_day = start_day + interval

print_interval(start_day, interval, end_day)

now = datetime.now()
interval = timedelta(hours=8, minutes=15, seconds=30)
end_time = now + interval
print_interval(now, interval, end_time)


def calculate_days(date_of_birth):
    today = datetime.today()
    result = today - date_of_birth
    print("".rjust(50, "."))
    print("Your time's life")
    print("".rjust(50, "."))

    print("Result: ", result)
    print("Days: ", result.days)
    print("Seconds:", result.seconds)
    print("Total hours:", result.total_seconds() / 3600)
    print("Total minutes:", result.total_seconds() / 60)


calculate_days(datetime(1986, 7, 12))
