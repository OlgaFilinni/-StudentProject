winners = []
file = open("first_tour.txt")
pass_score = int(file.readline())
for line in file:
    records_player = line.strip().split(" ")
    records_player[1] = f"{records_player[1][:1]}."
    records_player[2] = int(records_player[2])
    if int(records_player[2]) > pass_score:
        winners.append(records_player)
file.close()

count_players = len(winners)
print(winners)
# winners.sort(key=lambda x: -x[2])
for _ in range(len(winners)):
    for j in range(len(winners) - 1):
        if winners[j][2] < winners[j + 1][2]:
            winners[j + 1], winners[j] = winners[j], winners[j + 1]

print(winners)

second_file = open("second_tour.txt", "w", encoding="utf-8")
second_file.write(f"Kоличество участников {count_players} \n")
for i, record in enumerate(winners):
    second_file.write(f"{i + 1}) {record[1]} {record[0]} {record[2]} \n")
