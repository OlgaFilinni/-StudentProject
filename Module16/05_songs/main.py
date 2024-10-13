violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
user_list = []
minutes = 0
count_track = int(input("Сколько песен выбрать? "))
for track in range(count_track):
    print("Название", str(track+1) + "-й песни: ", end = "")
    name_track = input()
    user_list.append(name_track)

for info_songs in violator_songs:
    for song in user_list:
        if info_songs[0] == song:
            minutes += info_songs[1]

print("Общее время звучания песен: ", minutes)

