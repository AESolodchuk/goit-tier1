import calendar

dic = {1: "aleksey", 5: "solod", 2: "fuck"}

for key, value in dic.items():
    day_name = calendar.day_name[key]
    print(f"Day {key}: {value} - {day_name}")
