import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = "https://www.kinopoisk.ru/lists/top250/"
r = requests.get(url)
r.text

soup = BeautifulSoup(r.text, 'lxml')
link = "https://www.kinopoisk.ru"+soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').get('href')
link

russian_name = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__name').text
russian_name

original_name = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__original-name').text
original_name

country = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').find('span', class_='selection-film-item-meta__meta-additional-item').text
country

film_type = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').findAll('span', class_='selection-film-item-meta__meta-additional-item')[1].text
film_type

rate = soup.find('div', class_='desktop-rating-selection-film-item').find('span', class_='rating__value rating__value_positive').text
rate

data = []

for p in range(1, 6):
    print(p)

    url = f"https://www.kinopoisk.ru/lists//top250/?page={p}tab=all"
    r = requests.get(url)
    sleep(3)
    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.findAll('div', class_='desktop-rating-selection-film-item')

    for film in films:
        link = "https://www.kinopoisk.ru"+fiml.find('a', class_='selection-film-item-meta__link').get('href')
        russian_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__name').text
        original_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__original-name').text
        country = film.find('a', class_='selection-film-item-meta__link').find('span', class_='selection-film-item-meta__meta-additional-item').text
        film_type = film.find('a', class_='selection-film-item-meta__link').findAll('span', class_='selection-film-item-meta__meta-additional-item')[1].text
        try:
            rate = film.find('span', class_='rating__value rating__value_positive').text
        except:
            rate = '-'

    data.append([link, russian_name, original_name, country, film_type, rate])


header = ['link', 'russian_name', 'original_name', 'country', 'film_type', 'rate']

df = pd.DataFrame(data, columns=header)
df.to_csv('/Users/MIRA/Desktop/kinopoisk_data.csv', sep=";", encoding="utf8")









