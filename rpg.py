import os

class Game:
    def __init__(self, name: str):
        self.player = Player(name)
        self.map = Map()

    def show_move_options(self):
        return input("\n1) Move forward\n2) Move back\n3) Move up\n4) Move down\n>")

    def move_player(self):
        action = self.show_move_options()
        proposed_position = list(self.map.current_pos)
        if action == "1":
            proposed_position[1] += 1
        elif action == "2":
            proposed_position[1] -= 1
        elif action == "3":
            proposed_position[0] -= 1
        elif action == "4":
            proposed_position[0] += 1
        else:
            input("Invalid option. Press any key to continue.")

        self.map.move_player(proposed_position)
        self.proceed()

    def proceed(self):
        os.system('printf "\033c"')
        self.map.display_map()
        self.move_player()

class Player:
    def __init__(self, name: str):
        self.name = name

class Room:
    def __init__(self):
        self.description = f"This is a room."
        self.player_is_here = False
        self.end_room = False

    def show(self):
        result = "[   ]"
        if self.end_room is True:
            result = "[end]"
        if self.player_is_here is True:
            result = "[ x ]"
        return result

class Map:
    def __init__(self, height=5, length=5):
        self.height = height
        self.length = length
        self.layout = []
        self.create_map()
        self.current_pos = [self.height - 1, 0]
        self.layout[self.current_pos[0]][self.current_pos[1]].player_is_here = True
        self.layout[0][-1].end_room = True

    def move_player(self, proposed_position):
        try:
            if 0 > proposed_position[0] or proposed_position[0] >= self.height or 0 > proposed_position[1] or proposed_position[1] >= self.length:
                raise ValueError("Move out of bounds")

            self.layout[proposed_position[0]][proposed_position[1]].player_is_here = True
            self.layout[self.current_pos[0]][self.current_pos[1]].player_is_here = False
            self.current_pos = proposed_position
        except:
            input("Your move is invalid, please try again. Press any key.")

    def create_map(self):
        for x in range(self.height):
            self.layout.append([Room() for y in range(self.length)])

    def display_map(self):
        for x in range(self.height):
            for y in range(self.length):
                print(self.layout[x][y].show(), end=" ")
            print("")

def main():
    # input_name = input("What is your name? Press Enter to select the default name.")
    # player_name = input_name if input_name is not "" else "Chadwick Feeserton"
    player_name = "Chadwick Feeserton"
    game = Game(player_name)
    game.proceed()
    game.move_player()



main()
