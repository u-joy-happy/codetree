n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class WeatherInfo:
    def __init__(self, date, day, weather) :
        self.date = date
        self.day = day
        self.weather = weather

weather_info = [ WeatherInfo(date[i], day[i], weather[i]) for i in range(n)]

target_idx = -1
for idx, wi in enumerate(weather_info) :
    if wi.weather == 'Rain':
        if target_idx == -1 or weather_info[target_idx].date > wi.date :
            target_idx = idx

print(weather_info[target_idx].date, weather_info[target_idx].day, weather_info[target_idx].weather)