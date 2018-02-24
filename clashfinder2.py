from clashfinder import get_list as get_list
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests

api_key = 'AIzaSyBIu_ZJ86elyc69_KoXnW7Aoho1ZeBGzBQ'
cse_id = '003944353991449405587:vtjbgnaurd4'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    try:
        return res['items']
    except (KeyError, IndexError):
        return []


def execute_search():
    artist_list = get_list()
    review_urls = []
    for artist in artist_list:
        res = google_search(search_term='"' + artist + '"' + ' album review site:pitchfork.com',
                            api_key=api_key, cse_id=cse_id, num=2)

        try:
            if 'review' in res[0]['link']:
                review_urls.append(res[0]['link'])
            elif 'review' not in res[0]['link']:
                review_urls.append(res[1]['link'])
            else:
                review_urls.append('N/A')
                continue
        except (KeyError, IndexError):
                review_urls.append('N/A')
                continue
    return review_urls


def building_lists():
    album_names = []
    scores_list = []
    new_artist_list = []
    for review_url in execute_search():
        try:
            url = review_url
            html = requests.get(url)
            view_html = html.content
            soup = BeautifulSoup(view_html, 'html.parser')

            album = soup.find('h1', attrs={'class': 'single-album-tombstone__review-title'})
            album_name = album.text
            album_names.append(album_name)

            artist = soup.find('ul', attrs={'class': 'artist-links artist-list single-album-tombstone__artist-links'})
            artist_name = artist.text
            new_artist_list.append(artist_name)

            score = soup.find('span', {'class': 'score'})
            score_number = score.text
            scores_list.append(score_number)

        except:
            new_artist_list.append('N/A')
            album_names.append('N/A')
            scores_list.append('N/A')
    return new_artist_list, album_names, scores_list

