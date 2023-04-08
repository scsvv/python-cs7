weather_state ="sunny"
time=12

if time > 19 or time <= 6:
    print("Шторы закрыты")
elif (weather_state=="sunny" or weather_state=="cloudy") and time >= 17:
    print("Закрываю шторы")
else:
    print("Шторы открыты")



