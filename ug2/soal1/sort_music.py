songs = [
    {"title": "Golden Hour", "artist": "JVKE", "genre": "Pop", "views": 980000},
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "views": 2500000},
    {"title": "Snooze", "artist": "SZA", "genre": "R&B", "views": 1200000},
    {"title": "N95", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "views": 850000},
    {"title": "As It Was", "artist": "Harry Styles", "genre": "Pop", "views": 2100000},
    {"title": "Kill Bill", "artist": "SZA", "genre": "R&B", "views": 1750000}
]

def sort_by_views(songs):
    res = songs.copy()
    for i in range(len(res)):
        for j in range(len(res) - 1 - i):
            if res[j]["views"] < res[j + 1]["views"]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res
def sort_by_favourite_genre(songs, favourite_genre):
    res = songs.copy()
    for i in range(len(res)):
        for l in range(len(res) - 1 - i):
            if res[l]["genre"] != favourite_genre and res[l + 1]["genre"] == favourite_genre:
                res[l], res[l + 1] = res[l + 1], res[l]
    return res
print("=== SORT BY VIEWS ===")

result_views = sort_by_views(songs)

for song in result_views:
    print(song["title"], "-", song["views"], "views")


print("\n=== SORT BY FAVOURITE GENRE ===")

favourite_genre = "POP"

result_genre = sort_by_favourite_genre(songs, favourite_genre)

for song in result_genre:
    print(song["title"], "-", song["genre"])