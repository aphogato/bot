from requests import get
from bs4 import BeautifulSoup  

from handlers.translation import correct_translation

BASE_URL = 'https://pogoda.mail.ru/prognoz/#/14dney/'
HEADERS = {  
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': '*/*'
    }

def check_city(city):
    url = BASE_URL.replace('#', correct_translation(city))
    return get(url, headers=HEADERS).status_code == 200


def get_weather_data(city, class_name=None, element_id=None):
    url = BASE_URL.replace('#', correct_translation(city))
    html = get(url, headers=HEADERS) 

    soup = BeautifulSoup(html.text, 'html.parser')

    if element_id:
        element = soup.find('div', id=element_id)
        return element.text
    
    if class_name:
        elements = soup.find_all('span', class_=class_name)
        return [elem.text for elem in elements]


def date(day): 
    return get_weather_data("moskva", element_id=f"d-{day}")


def weather(city): 
    return get_weather_data(city, class_name='text text_block text_bold_medium margin_bottom_10')


def temperature(city):
    return get_weather_data(city, class_name='text text_block text_light_normal text_fixed color_gray')


def osadki(city):
    return get_weather_data(city, class_name='text text_block text_light_normal text_fixed')
