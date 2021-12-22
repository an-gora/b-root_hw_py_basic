from datetime import date
import calendar

name = "Anastasiia"
current_day = date.today()
current_week_day = calendar.day_name[current_day.weekday()]
print(f"Good day {name}! {current_week_day} is a perfect day " \
      f"to learn spme python")
