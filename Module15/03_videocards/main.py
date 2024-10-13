count_video_card = int(input("Введите общее количество видеокарт: "))
list_video_card = []
new_list_video_card = []

for card in range(count_video_card):
    id_card = int(input("Видеокарта: "))
    list_video_card.append(id_card)

old_id_card = list_video_card[0]
for i in range(count_video_card):
    if list_video_card[i] > old_id_card:
        old_id_card = list_video_card[i]

for i in range(count_video_card):
    if list_video_card[i] < old_id_card:
        new_list_video_card.append(list_video_card[i])
print("Старый список видеокарт: ", list_video_card)
print(new_list_video_card)





