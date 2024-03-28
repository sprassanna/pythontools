import requests
import datetime as dt
import smtplib
import time

EMAIL = ''

PASSWORD = ''

ISS_URL = 'http://api.open-notify.org/iss-now.json'

SUN_URL = 'https://api.sunrise-sunset.org/json'



MY_LAT = -45
MY_LANG = -135

parameters = {
    'lat':MY_LAT,
    'lng':MY_LANG,
    'formatted':0
}

response2 = requests.get(url=SUN_URL,params=parameters)
response2.raise_for_status()
results = response2.json()['results']

while True:

    response1 = requests.get(url=ISS_URL)
    response1.raise_for_status()
    iss_position = response1.json()['iss_position']

    iss_lat = int(round(float(iss_position['latitude'])))
    iss_lang = int(round(float(iss_position['longitude'])))

    print((iss_lat,iss_lang))


    print(results)

    sunrise = results['sunrise']
    sunset = results['sunset']

    print(sunset.split('T')[1])

    sunset_time = sunset.split('T')[1]
    print(sunset_time)
    sunset_hour = sunset_time.split(':')[0]
    sunset_min = sunset_time.split(':')[1]


    print(f'sunset {(sunset_hour,sunset_min)}')

    my_lat_diff = abs(MY_LAT - iss_lat)

    my_lang_diff = abs(MY_LANG - iss_lang)

    print((my_lat_diff,my_lang_diff))

    if abs(my_lat_diff) <=5 or abs(my_lang_diff) <=5:
        now = dt.datetime.now()
        now_hr = now.hour
        now_minute = now.minute
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as connection:
            connection.login(user=EMAIL,password=PASSWORD)

            connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f'Subject:Step out \n \n Look out for the satellite')

    time.sleep(5)


