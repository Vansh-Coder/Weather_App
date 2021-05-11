import json
import config       # file containing api key
import requests
from tkinter import *
from datetime import datetime
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageEnhance

weather_app = Tk()
weather_app.title('Weather App')
weather_app.geometry("732x400")

with open('city.list.json', encoding='utf-8') as ls:
    data = json.load(ls)

cc_dict = {'Afghanistan': 'AF', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS', 'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ',
           'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahrain': 'BH',
           'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT', 
           'Bonaire, Sint Eustatius and Saba': 'BQ', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Brazil': 'BR', 'Brunei Darussalam': 'BN', 'Bulgaria': 'BG',
           'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cabo Verde': 'CV', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN',
           'Christmas Island': 'CX', 'Colombia': 'CO', 'Costa Rica': 'CR', 'Croatia': 'HR', 'Cuba': 'CU', 'Curaçao': 'CW', 'Cyprus': 'CY', 'Czechia': 'CZ',
           "Côte d'Ivoire": 'CI', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV', 'Equatorial Guinea': 'GQ',
           'Eritrea': 'ER', 'Estonia': 'EE', 'Eswatini': 'SZ', 'Ethiopia': 'ET', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF',
           'Gabon': 'GA', 'Georgia': 'GE', 'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL', 'Grenada': 'GD', 'Guadeloupe': 'GP',
           'Guam': 'GU', 'Guatemala': 'GT', 'Guernsey': 'GG', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Honduras': 'HN', 'Hong Kong': 'HK',
           'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT',
           'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kiribati': 'KI', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG',
           'Latvia': 'LV', 'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Liechtenstein': 'LI', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macao': 'MO',
           'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU',
           'Mayotte': 'YT', 'Mexico': 'MX', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME', 'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM',
           'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF',
           'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Pitcairn': 'PN',
           'Poland': 'PL', 'Portugal': 'PT', 'Puerto Rico': 'PR', 'Qatar': 'QA', 'Republic of North Macedonia': 'MK', 'Romania': 'RO', 'Rwanda': 'RW', 'Réunion': 'RE',
           'Saint Barthélemy': 'BL', 'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Saint Kitts and Nevis': 'KN', 'Saint Lucia': 'LC', 'Saint Pierre and Miquelon': 'PM',
           'Saint Vincent and the Grenadines': 'VC', 'Samoa': 'WS', 'San Marino': 'SM', 'Sao Tome and Principe': 'ST', 'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS',
           'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA',
           'South Georgia and the South Sandwich Islands': 'GS', 'Republic of South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Suriname': 'SR',
           'Svalbard and Jan Mayen': 'SJ', 'Sweden': 'SE', 'Switzerland': 'CH', 'Syrian Arab Republic': 'SY', 'Tajikistan': 'TJ', 'Thailand': 'TH', 'Timor-Leste': 'TL',
           'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Tuvalu': 'TV', 'Uganda': 'UG',
           'Ukraine': 'UA', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Vietnam': 'VN', 'British Virgin Islands': 'VG', 'U.S. Virgin Islands': 'VI',
           'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW', 'Åland Islands': 'AX', 'Kosovo': 'XK', 'Bahamas': 'BS',
           'Bolivia': 'BO', 'Cayman Islands': 'KY', 'Central African Republic': 'CF', 'Cocos (Keeling) Islands': 'CC', 'Comoros': 'KM', 'Democratic Republic of Congo': 'CD',
           'Republic of Congo': 'CG', 'Cook Islands': 'CK', 'Dominican Republic': 'DO', 'Falkland Islands (Malvinas)': 'FK', 'Faroe Islands': 'FO',
           'French Southern Territories': 'TF', 'Gambia': 'GM', 'Holy See': 'VA', 'Iran': 'IR', 'North Korea': 'KP', 'South Korea': 'KR',
           "Lao People's Democratic Republic": 'LA', 'Marshall Islands': 'MH', 'Micronesia': 'FM', 'Moldova': 'MD', 'Netherlands': 'NL', 'Niger': 'NE',
           'Northern Mariana Islands': 'MP', 'Palestine': 'PS', 'Philippines': 'PH', 'Russia': 'RU', 'Saint-Martin': 'MF', 'Sint Maarten': 'SX', 'Republic of Sudan': 'SD',
           'Taiwan': 'TW', 'Tanzania': 'TZ', 'Turks and Caicos Islands': 'TC', 'United Arab Emirates': 'AE', 'United Kingdom': 'GB', 'United States of America': 'US',
           'Venezuela': 'VE'}
cc_values = list(cc_dict.keys())
cc_values.sort()

city_dict = {}
city_id = 0

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
image_url = 'https://openweathermap.org/img/wn/'
api_key = config.API_KEY

def func_country(event_country):
    global city_dict

    current_country = country.get()
    country_code = cc_dict[current_country]
    city_dict = {}
    for i in data:
        if i['country'] == country_code:
            city_dict[i['name']] = i['id']
    city_values = list(city_dict.keys())
    city_values.sort()
    city_dropdown['values'] = city_values
    city_dropdown.set('(Select a city)')

def func_city(event_city):
    global city_dict, city_id

    current_city = city.get()
    if current_city[1:7] != 'Select':
        city_id = city_dict[current_city]

def selection():
    current_choice = choice.get()
    if current_choice == 1:
        city_dropdown.config(state='readonly')
        entry_zipcode.config(state=DISABLED)
    elif current_choice == 2:
        entry_zipcode.config(state=NORMAL)
        city_dropdown.config(state='disabled')

def check_weather():
    global city_id, base_url, cc_dict, api_key

    f = True
    current_country = country.get()
    current_choice = choice.get()
    current_zipcode = entry_zipcode.get()
    if current_country[1:7] == 'Select':
        f = False
        messagebox.showinfo('Empty country error !', 'Please select a country first and then try again !')
    if f is True and current_choice == 1 and city_id == 0:
        f = False
        messagebox.showinfo('Empty city error !', 'Please select a city first and then try again !')
    if f is True and current_choice == 2 and len(entry_zipcode.get()) == 0:
        f = False
        messagebox.showinfo('Empty zipcode error !', 'Please enter a zipcode and then try again !')
    if f is True and current_choice == 2 and current_zipcode.isalnum() is False:
        f = False
        messagebox.showinfo('Invalid zipcode error !', 'The zipcode "' + current_zipcode + '" is invalid. Please enter a valid zipcode and try again !')
    if f is True:
        url = ''
        if current_choice == 1:
            url = base_url + 'id=' + str(city_id) + '&units=metric' + '&appid=' + api_key
        elif current_choice == 2:
            country_code = cc_dict[current_country]
            url = base_url + 'zip=' + current_zipcode + ',' + country_code + '&units=metric' + '&appid=' + api_key
        if url != '':
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    api_response = response.json()
                    report_weather(api_response)
                elif response.status_code == 404 and current_choice == 2:
                    messagebox.showinfo('Zipcode error !', 'Either the zipcode entered is invalid or the weather of that area has not been checked. If the problem persists, try checking weather with the city name instead.')
                else:
                    messagebox.showerror('Technical error !', 'There is some technical error at the moment, please try again later !')
            except:
                messagebox.showerror('Technical error !', 'Something went wrong, please check your internet connection and try again !')

def report_weather(weather_report):
    info = weather_report.keys()
    if 'name' in info and len(weather_report['name']) > 0:
        label_location.config(text='Location : ' + weather_report['name'] + ', ' + country.get())
    elif city.get()[1:7] != 'Select':
        label_location.config(text='Location : ' + city.get() + ', ' + country.get())
    else:
        label_location.config(text='Location : ' + country.get())
    if 'dt' in info and len(str(weather_report['dt'])) > 0:
        time = datetime.fromtimestamp(weather_report['dt']).strftime('%H:%M:%S')
        if time[0] == '0':
            time += ' A.M.'
        else:
            time += ' P.M.'
        label_time.config(text='Last checked at : ' + time)
    else:
        label_time.config(text='Last checked at : N/A')
    if 'weather' in info and len(weather_report['weather'][0]) > 0:
        weather_report['weather'] = weather_report['weather'][0]
        if 'main' in weather_report['weather'].keys():
            label_type.config(text='Weather type : ' + weather_report['weather']['main'])
        else:
            label_type.config(text='Weather type : N/A')
        if 'description' in weather_report['weather'].keys():
            label_description.config(text='Description : ' + weather_report['weather']['description'])
        else:
            label_description.config(text='Description : N/A')
        if 'icon' in weather_report['weather'].keys():
            image_name = weather_report['weather']['icon']
            image_link = image_url + image_name + '@2x.png'
            image = Image.open(requests.get(image_link, stream=True).raw).resize((150, 150))
            enhancer = ImageEnhance.Contrast(image)
            image_enhanced = enhancer.enhance(1.5)
            image_tk = ImageTk.PhotoImage(image_enhanced)
            label_image.config(image=image_tk)
            label_image.image = image_tk
        else:
            label_image.config(image=None)
    else:
        label_type.config(text='Weather type : N/A')
        label_description.config(text='Description : N/A')
        label_image.config(image=None)
    if 'main' in info and len(weather_report['main']) > 0:
        main_info = weather_report['main'].keys()
        if 'temp' in main_info:
            label_temperature.config(text='Temperature : ' + str(weather_report['main']['temp']) + '°C')
        else:
            label_temperature.config(text='Temperature : N/A')
        if 'feels_like' in main_info:
            label_feelsTemp.config(text='Feels like : ' + str(weather_report['main']['feels_like']) + '°C')
        else:
            label_feelsTemp.config(text='Feels like : N/A')
        if 'temp_min' in main_info:
            label_minTemp.config(text='Min. Temperature : ' + str(weather_report['main']['temp_min']) + '°C')
        else:
            label_minTemp.config(text='Min. Temperature : N/A')
        if 'temp_max' in main_info:
            label_maxTemp.config(text='Max. Temperature : ' + str(weather_report['main']['temp_max']) + '°C')
        else:
            label_maxTemp.config(text='Max. Temperature : N/A')
        if 'humidity' in main_info:
            label_humidity.config(text='Humidity : ' + str(weather_report['main']['humidity']) + '%')
        else:
            label_maxTemp.config(text='Humidity : N/A')
    else:
        label_temperature.config(text='Temperature : N/A')
        label_feelsTemp.config(text='Feels like : N/A')
        label_minTemp.config(text='Min. Temperature : N/A')
        label_maxTemp.config(text='Max. Temperature : N/A')
    if 'wind' in info and len(weather_report['wind']) > 0:
        if 'speed' in weather_report['wind'].keys():
            label_windSpeed.config(text='Wind speed : ' + str(weather_report['wind']['speed']) + ' m/s')
        else:
            label_windSpeed.config(text='Wind speed : N/A')
        if 'deg' in weather_report['wind'].keys():
            degrees = weather_report['wind']['deg']
            direction = ''
            if degrees == 0 or degrees == 360:
                direction = 'North'
            elif degrees == 90:
                direction = 'East'
            elif degrees == 180:
                direction = 'South'
            elif degrees == 270:
                direction = 'West'
            elif 0 < degrees < 90:
                direction = 'North-East'
            elif 90 < degrees < 180:
                direction = 'South-East'
            elif 180 < degrees < 270:
                direction = 'South-West'
            elif 270 < degrees < 360:
                direction = 'North-West'
            label_direction.config(text='Wind direction : ' + direction + ' (' + str(degrees) + '°' + ')')
        else:
            label_direction.config(text='Wind direction : N/A')
    else:
        label_windSpeed.config(text='Wind speed : N/A')
        label_direction.config(text='Wind direction : N/A')
    if 'clouds' in info and len(weather_report['clouds']) > 0:
        if 'all' in weather_report['clouds'].keys():
            label_clouds.config(text='Cloudiness : ' + str(weather_report['clouds']['all']) + '%')
        else:
            label_clouds.config(text='Cloudiness : N/A')
    else:
        label_clouds.config(text='Cloudiness : N/A')
    if 'sys' in info and len(weather_report['sys']) > 0:
        if 'sunrise' in weather_report['sys'].keys():
            time = datetime.fromtimestamp(weather_report['sys']['sunrise']).strftime('%H:%M:%S')
            if time[0] == '0':
                time += ' A.M.'
            else:
                time += ' P.M.'
            label_sunrise.config(text='Sunrise time : ' + time)
        else:
            label_sunrise.config(text='Sunrise time : N/A')
        if 'sunset' in weather_report['sys'].keys():
            time = datetime.fromtimestamp(weather_report['sys']['sunset']).strftime('%H:%M:%S')
            if time[0] == '0':
                time += ' A.M.'
            else:
                time += ' P.M.'
            label_sunset.config(text='Sunset time : ' + time)
        else:
            label_sunset.config(text='Sunset time : N/A')
    else:
        label_sunrise.config(text='Sunset time : N/A')
        label_sunset.config(text='Sunrise time : N/A')
    if 'rain' in info and len(weather_report['rain']) > 0:
        if '3h' in weather_report['rain'].keys():
            label_rain.config(text='Rain volume : ' + str(weather_report['rain']['3h']) + ' mm' + ' (for last 3 hrs)')
        elif '1h' in weather_report['rain'].keys():
            label_rain.config(text='Rain volume : ' + str(weather_report['rain']['1h']) + ' mm' + ' (for last 1 hr)')
        else:
            label_rain.config(text='Rain volume : N/A')
    else:
        label_rain.config(text='Rain volume : N/A')
    if 'snow' in info and len(weather_report['snow']) > 0:
        if '3h' in weather_report['snow'].keys():
            label_snow.config(text='Snow volume : ' + str(weather_report['snow']['3h']) + ' mm' + ' (for last 3 hrs)')
        elif '1h' in weather_report['snow'].keys():
            label_snow.config(text='Snow volume : ' + str(weather_report['snow']['1h']) + ' mm' + ' (for last 1 hr)')
        else:
            label_snow.config(text='Snow volume : N/A')
    else:
        label_snow.config(text='Snow volume : N/A')

def info_about(query):
    if query == 1:
        messagebox.showinfo('Feels like temperature info !', 'The "feels like" temperature is a measurement of how hot or cold it really feels like outside, to bare skin. It relies on several environmental data including the ambient air temperature, relative humidity, and wind speed.')
    elif query == 2:
        messagebox.showinfo('N/A info !', '"N/A" means the phenomena/parameter has not taken place in the specified area yet (most likely), or has not been measured yet.')

label_country = Label(weather_app, text='Select your country :', font=('Times New Roman', '13'))
label_city = Label(weather_app, text='Select your city :', font=('Times New Roman', '13'))
label_OR = Label(weather_app, text='OR', font=('Times New Roman', '13'))
label_zipcode = Label(weather_app, text='Enter your zipcode :', font=('Times New Roman', '13'))

choice = IntVar()
button_city = Radiobutton(weather_app, variable=choice, value=1, command=selection)
button_zipcode = Radiobutton(weather_app, variable=choice, value=2, command=selection)

country = StringVar()
country_dropdown = ttk.Combobox(weather_app, width=30, textvariable=country, values=cc_values, state='readonly')

city = StringVar()
city_dropdown = ttk.Combobox(weather_app, width=33, textvariable=city, values=['(Select a country first)'], state='readonly')

entry_zipcode = Entry(weather_app, width=15, borderwidth=2, font=('Times New Roman', '11'))

button_check = Button(weather_app, text='Check Weather', width=12, font=('Times New Roman', '12'), fg='#009933', activeforeground='#00802b', activebackground='#cccccc', command=check_weather)

label_location = Label(weather_app, text='Location :', font=('Times New Roman', '13'))
label_time = Label(weather_app, text='Last checked at :', font=('Times New Roman', '13'))
label_type = Label(weather_app, text='Weather type :', font=('Times New Roman', '13'))
label_description = Label(weather_app, text='Description :', font=('Times New Roman', '13'))

label_temperature = Label(weather_app, text='Temperature :', font=('Helvetica', '11'))
label_feelsTemp = Label(weather_app, text='Feels like :', font=('Helvetica', '11'))
label_minTemp = Label(weather_app, text='Min. Temperature :', font=('Helvetica', '11'))
label_maxTemp = Label(weather_app, text='Max. Temperature :', font=('Helvetica', '11'))

label_humidity = Label(weather_app, text='Humidity :', font=('Helvetica', '11'))
label_windSpeed = Label(weather_app, text='Wind speed :', font=('Helvetica', '11'))
label_direction = Label(weather_app, text='Wind direction :', font=('Helvetica', '11'))
label_clouds = Label(weather_app, text='Cloudiness :', font=('Helvetica', '11'))

label_sunrise = Label(weather_app, text='Sunrise time :', font=('Helvetica', '11'))
label_sunset = Label(weather_app, text='Sunset time :', font=('Helvetica', '11'))
label_rain = Label(weather_app, text='Rain volume :', font=('Helvetica', '11'))
label_snow = Label(weather_app, text='Snow volume :', font=('Helvetica', '11'))

label_image = Label(weather_app)
button_feels = Button(weather_app, text='?', width=2, padx=2, font=('Georgia', '10'), activebackground='#cccccc', command=lambda: info_about(1))
label_NA = Label(weather_app, text='(N/A)', font=('Times New Roman', '13'))
button_NA = Button(weather_app, text='?', width=2, padx=2, font=('Georgia', '10'), activebackground='#cccccc', command=lambda: info_about(2))
button_exit = Button(weather_app, text='Exit', width=4, font=('Times New Roman', '13'), fg='#ff3333', activeforeground='#ff1a1a', activebackground='#cccccc', command=weather_app.destroy)

label_country.place(x=33, y=5)
label_city.place(x=283, y=5)
label_OR.place(x=486, y=16)
label_zipcode.place(x=565, y=5)

button_city.place(x=258, y=5)
button_zipcode.place(x=539, y=5)

country_dropdown.place(x=9, y=34)
city_dropdown.place(x=230, y=34)

entry_zipcode.place(x=572, y=34)

button_check.place(x=283, y=74)

label_location.place(x=5, y=130)
label_time.place(x=5, y=155)
label_type.place(x=5, y=180)
label_description.place(x=5, y=205)

label_temperature.place(x=5, y=245)
label_feelsTemp.place(x=5, y=270)
label_minTemp.place(x=5, y=295)
label_maxTemp.place(x=5, y=320)

label_humidity.place(x=225, y=245)
label_windSpeed.place(x=225, y=270)
label_direction.place(x=225, y=295)
label_clouds.place(x=225, y=320)

label_sunrise.place(x=465, y=245)
label_sunset.place(x=465, y=270)
label_rain.place(x=465, y=295)
label_snow.place(x=465, y=320)

label_image.place(x=500, y=88)
button_feels.place(x=142, y=267)
label_NA.place(x=5, y=368)
button_NA.place(x=52, y=366)
button_exit.place(x=679, y=361)

button_city.select()

country_dropdown.set('(Select a country)')
country_dropdown.bind('<<ComboboxSelected>>', func_country)

city_dropdown.current(0)
city_dropdown.bind('<<ComboboxSelected>>', func_city)

entry_zipcode.config(state=DISABLED)

weather_app.resizable(False, False)
weather_app.mainloop()
