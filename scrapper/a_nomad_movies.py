import requests

movie_ids = [238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430]
all_movie_info = []


def get_movie(movie_ids):

    url = "https://nomad-movies.nomadcoders.workers.dev/movies/"
    for i in movie_ids:
        response = requests.get(url + str(i))
        data = response.json()
        movie_info = {
            "title": data["title"],
            "overview": data["overview"],
            "vote_average": data["vote_average"],
        }
        all_movie_info.append(movie_info)


get_movie(movie_ids)

for i in range(len(all_movie_info)):
    print("\n")
    print(all_movie_info[i])
