import requests
from bs4 import BeautifulSoup
##testinbggggg

def get_list():
    # url = 'https://lineup.primaverasound.es/2018_artists'
    url = 'http://www.efestivals.co.uk/festivals/primavera/2018/lineup.shtml'

    html = requests.get(url)
    view_html = html.content
    soup = BeautifulSoup(view_html, 'html.parser')
    artists = soup.find_all('div', attrs={'class': 'band'}, limit=6)
    artist_list = [i.text.strip()[4:] for i in artists]

    cleaned_list = []

    for artist in artist_list:
        new_name = artist[:-5]
        cleaned_list.append(new_name)

    return artist_list
