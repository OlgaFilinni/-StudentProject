# 1. Класс, который будет описывать поле игры.

class Board:

    #     #  Класс поля, который создаёт у себя экземпляры клетки.
    def __init__(self, players):
        self.players = players
        self.size = 3
        self.all_cells = [Cell() for _ in range(self.size ** 2)]
        self.num_player = 0

    #     #  Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
    def print_board(self):
        res_text = ''
        for player in self.players:
            res_text += f"{player.get_name()} => {player.get_symbol()}\n"
        for i in range(self.size ** 2):
            if self.all_cells[i].get_symbol():
                res_text += f"[ {self.all_cells[i].get_symbol()} ]"
            else:
                res_text += f"[ {i} ]"
            if (i + 1) % self.size == 0:
                res_text += '\n'
        print(res_text)

    def clear_board(self):
        for cell in self.all_cells:
            cell.set_none()

    #     #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята, меняет её состояние. Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
    def check_nones(self):
        """Если есть зотябы 1 None, можем ходить"""
        for cell in self.all_cells:
            if cell.get_symbol() is None:
                return True
        return False

    def check_cell(self, player):
        """Проверяем возможность походить"""
        if self.all_cells[player.get_last_step()].get_symbol():  # если клетка, куда выбрал идти игрок уже имеет символ
            print('Не, сюда нельзя')
            return False
        self.all_cells[player.get_last_step()].set_symbol(player.get_symbol())  # клетку передаем
        return True

    def next_step(self):
        player = self.players[self.num_player % len(self.players)]
        print(f'Ходит {player.get_name()}')
        while True:
            cell_num = int(input('Введите номер ячейки: '))
            player.set_last_step(cell_num)
            if self.check_cell(player):
                break
        self.num_player += 1


#     #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False. True — если один из игроков победил, False — если победителя нет.


# 2. Класс, который будет описывать одну клетку поля:

class Cell:

    def __init__(self):
        self._cell_symbol = None

    def get_symbol(self):
        return self._cell_symbol

    def set_symbol(self, symbol):
        self._cell_symbol = symbol

    def set_none(self):
        self._cell_symbol = None


class Player:
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol
        self._last_step = None

    def get_symbol(self):
        return self._symbol

    def get_name(self):
        return self._name

    def get_last_step(self):
        return self._last_step

    def set_last_step(self, step):
        self._last_step = step


#     #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки). Введённый номер нужно обязательно проверить.


# 4. Класс, который управляет ходом игры:

class Game:

    def __init__(self, board, players):
        #     # класс «Игры» содержит атрибуты:
        self.state_game = True
        #     # состояние игры,
        self.players = players
        #     # игроки
        self.board = board
        #     # поле.
        self.num_player = 0

    #     # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    def check_win(self):
        """Проверяем наличие победителя"""
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i1, i2, i3 in wins:
            for player in self.players:
                # print(self.all_cells[i1].get_symbol(), self.all_cells[i2].get_symbol(), self.all_cells[i3].get_symbol(), player.get_symbol())
                if self.board.all_cells[i1].get_symbol() == self.board.all_cells[i2].get_symbol() == \
                        self.board.all_cells[i3].get_symbol() == player.get_symbol():
                    return player._name
        return False

    def run_game(self):
        self.board.print_board()
        while True:
            res_check_win = self.check_win()
            if res_check_win:
                print(f'Победитель {res_check_win}')
                break
            if not self.board.check_nones():
                print('Ничья')
                break
            self.board.next_step()
            self.board.print_board()


#     # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.

#     # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.

def get_list_players():
    players = []
    for symbol in 'XO':
        name = f"player_{symbol}"  # input(F'Введите имя игрока, который будет ходить за {symbol}: ')
        players.append(Player(name=name, symbol=symbol))
    return players


players = get_list_players()
board = Board(players)
game = Game(board, players)
game.run_game()
while True:
    answer = input("Хотите продолжить? да/нет ").lower()

    if answer == "да":
        board.clear_board()
        game.run_game()
    else:
        print("Игра окончена")
        break






