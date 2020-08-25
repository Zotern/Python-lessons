import requests

# TODO for morning the_weather['forecasts'][0]['parts']['morning']['temp_avg'],\
# TODO for day the_weather['forecasts'][0]['parts']['day']['temp_avg'],\
# TODO for evening the_weather['forecasts'][0]['parts']['evening']['temp_avg'])

weather_conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно',
                      'overcast': 'пасмурно', 'light-rain': 'небольшой дождь',
                      'partly-cloudy-and-light-rain': 'небольшой дождь', 
                      'partly-cloudy-and-rain': 'дождь', 'rain': 'дождь',
                      'overcast-and-rain': 'сильный дождь', 
                      'overcast-thunderstorms-with-rain': 'сильный дождь, гроза', 
                      'cloudy-and-light-rain': 'небольшой дождь',
                      'overcast-and-light-rain': 'небольшой дождь',
                      'cloudy-and-rain': 'дождь', 'overcast-and-wet-snow': 'дождь со снегом',
                      'partly-cloudy-and-light-snow': 'небольшой снег', 'partly-cloudy-and-snow': 'снег',
                      'overcast-and-snow': 'снегопад', 'cloudy-and-light-snow': 'небольшой снег',
                      'overcast-and-light-snow': 'небольшой снег', 'cloudy-and-snow': 'снег'}

week = {'today': 0, 'in_1_day': 1,
        'in_2_days': 2, 'in_3_days': 3,
        'in_4_days': 4, 'in_5_days': 5,
        'in_6_days': 6}


def get_current_weather():
	url = 'https://api.weather.yandex.ru/v2/forecast?'
	headers = {'X-Yandex-API-Key':'31627a0d-8059-42a2-87aa-2037a0b63ccd', 'lat': '',
	           'lon': '', 'lang': 'json', 'limit': '1', 'hours': 'true', 'extra': 'true'}
	r = requests.get(url, headers=headers)
	the_weather = r.json()

	for i in weather_conditions:
		if the_weather['fact']['condition'] in i:
			the_weather['fact']['condition'] = weather_conditions[the_weather['fact']['condition']]

	if 'fact' in the_weather:
		try:
			return ([the_weather['fact']['temp'],
			         the_weather['fact']['feels_like'],
			         the_weather['fact']['condition'],
			         the_weather['fact']['wind_speed'],
			         the_weather['fact']['pressure_mm'],
			         the_weather['info']['url']])
		except (IndexError, TypeError):
			return 'Server Error'
	return 'Server Error'


def get_weather_for_times_of_day(time_of_date, date):
	url = 'https://api.weather.yandex.ru/v2/forecast?'
	headers = {'X-Yandex-API-Key':'31627a0d-8059-42a2-87aa-2037a0b63ccd', 'lat': '',
	           'lon': '', 'lang': 'json', 'limit': '1', 'hours': 'True', 'extra': 'True'}
	r = requests.get(url, headers=headers)
	the_weather = r.json()

	for i in weather_conditions:
		if the_weather['forecasts'][date]['parts'][time_of_date]['condition'] in i:
				the_weather['forecasts'][date]['parts'][time_of_date]['condition'] = weather_conditions[the_weather['forecasts'][date]['parts'][time_of_date]['condition']]

	if 'forecasts' in the_weather:
		try:
			return (the_weather['forecasts'][date]['date'],
			        the_weather['forecasts'][date]['parts'][time_of_date]['temp_avg'],
			        the_weather['forecasts'][date]['parts'][time_of_date]['condition'],
			        the_weather['forecasts'][date]['parts'][time_of_date]['feels_like'],
			        the_weather['forecasts'][date]['parts'][time_of_date]['wind_speed'],
			        the_weather['forecasts'][date]['parts'][time_of_date]['pressure_mm'])
		except (IndexError, TypeError):
			return 'Server Error'
	return 'Server Error'

		# TODO Weather for a day.

if __name__ == '__main__':
	weather = get_current_weather()
	print(weather)
	'''weather_of_night = get_weather_for_times_of_day('night', week['in_1_day'])
	print('Дата - {}\nТемпература ночью - {}°C\nОщущается как - {}°C\
		\n{}\nСкорость ветра - {}м/с\nДавление - {}мм'.format(weather_of_night[0], weather_of_night[1],
		                                                      weather_of_night[3], weather_of_night[2].title(),
		                                                      weather_of_night[4], weather_of_night[5]))

	weather_of_night = get_weather_for_times_of_day('morning', week['today'])
	print('Дата - {}\nТемпература утром - {}°C\nОщущается как - {}°C\
		\n{}\nСкорость ветра - {}м/с\nДавление - {}мм'.format(weather_of_night[0], weather_of_night[1],
		                                                      weather_of_night[3], weather_of_night[2].title(),
		                                                      weather_of_night[4], weather_of_night[5]))

	weather_of_night = get_weather_for_times_of_day('day', week['today'])
	print('Дата - {}\nТемпература днём - {}°C\nОщущается как - {}°C\
		\n{}\nСкорость ветра - {}м/с\nДавление - {}мм'.format(weather_of_night[0], weather_of_night[1],
		                                                      weather_of_night[3], weather_of_night[2].title(),
		                                                      weather_of_night[4], weather_of_night[5]))

	weather_of_night = get_weather_for_times_of_day('evening', week['today'])
	print('Дата - {}\nТемпература вечером - {}°C\nОщущается как - {}°C\
		\n{}\nСкорость ветра - {}м/с\nДавление - {}мм'.format(weather_of_night[0], weather_of_night[1],
		                                                      weather_of_night[3], weather_of_night[2].title(),
		                                                      weather_of_night[4], weather_of_night[5]))'''
