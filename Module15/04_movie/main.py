def in_list(list_films, film):
    for element in list_films:
        if element == film:
            return True


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
count = 0
user_list = []
count_film_like_user = int(input("Сколько фильмов хотите добавить? "))
while count_film_like_user:
    count_film_like_user -= 1
    name_film = input("Введите название фильма: ")
    if in_list(films, name_film):
        user_list.append(name_film)
    else:
        print("Ошибка: фильма", name_film, "у нас нет :(")

print("Ваш список любимых фильмов", user_list)

