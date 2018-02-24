from clashfinder2 import building_lists, execute_search

urls = execute_search()
new_artist_list, album_names, scores_list = building_lists()


def put_it_together():
    integer_scores = []
    for score in scores_list:
        try:
            int_score = float(score)
            integer_scores.append(int_score)
        except ValueError:
            integer_scores.append("N/A")

    sorted_and_ranked_dictionary = sorted([{'artist': art, 'album': alb, 'score': score, 'url': url}
                                           for art, alb, score, url in zip(new_artist_list, album_names, integer_scores,
                                                                           urls) if
                                           art != 'N/A'
                                           ], key=lambda k: k['score'], reverse=True)

    message = "Artist name is {0}, album is {1} and pitchfork score is {2} \n link is {3}"

    for item in sorted_and_ranked_dictionary:
        if item['artist'] != 'N/A':
            print(message.format(item['artist'], item['album'], item['score'], item['url']))


put_it_together()
