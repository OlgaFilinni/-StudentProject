str_h = input("Введите строку: ")


start = str_h.index("h")
stop = str_h.rindex("h")

revers_piece = str_h[start + 1: stop]
revers_piece = revers_piece[::-1]
print("Развёрнутая последовательность между первым и последним h: ", revers_piece)
