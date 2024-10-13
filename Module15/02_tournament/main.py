list_players = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
list_players_1_day = []
for i in range(len(list_players)):
    if i % 2 == 0:
        list_players_1_day.append(list_players[i])

print("Первый день: ", list_players_1_day )



