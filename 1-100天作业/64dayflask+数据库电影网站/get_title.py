import requests

def get_title(title):
    url = f"https://api.themoviedb.org/3/search/movie?query={title}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5NmViMGI0MjRiOTA5OTNlYzExZDcxMzk3MmY3ZDgwYiIsIm5iZiI6MTcyNDA1NDQwOS4wMzc2NjcsInN1YiI6IjY2YzJmODJlODlhMTI5ZGJmNzZlMzY5MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4cJEEWKOkuazQnWT6yBVkXCBm75aJRjSnqZfqtrY2aE",
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    data_list = []
    for x in data["results"]:
        # if not x['poster_path'] :
        data={
        'id' : x['id'],
        'img_url' : 'https://image.tmdb.org/t/p/original'+ str(x['poster_path']),
        'year' : x['release_date'],
        'title' : x['title'],
        'description' :x['overview']}
        data_list.append(data)
    return data_list
if __name__ == "__main__":
    print(get_title("复仇者联盟"))
