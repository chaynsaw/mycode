class Game:
    def __init__(self, name: str):
        self.player = Player(name)

class Player:
    def __init__(self, name: str):
        self.name = name

class Room:
    def __init__(self):
        self.description = f"This is a room."
        self.current_pos = False
        self.end_room = False

    def show(self):
        result = "[   ]"
        if self.end_room is True:
            result = "[end]"
        if self.current_pos is True:
            result = "[ x ]"
        return result

class Map:
    def __init__(self, height=5, length=5):
        self.height = height
        self.length = length
        self.layout = []
        self.create_map()
        self.layout[-1][0].current_pos = True
        self.layout[0][-1].end_room = True

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
    map = Map()
    # print(map.layout)
    # map.display_map()
    map.display_map()


main()
