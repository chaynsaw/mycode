import os
import random

ROOM_DESCRIPTIONS = [
    'A cold, dark room. It is dimly lit by a lone candlelight.',
    'A bright, dark room. There is no light source that you can think of.',
    'A bright, warm room. It feels cozy. You could fall asleep here.',
    'A dark, warm room. No idea what is generating warmth, certainly not the torch illuminating just enough the staircase up, and the doorways leading out.'
]


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
            input("Invalid option. Press enter to continue.")

        self.map.move_player(proposed_position)
        self.proceed()

    def begin(self):
        os.system('printf "\033c"')
        print("You awake with no memory of who you are in a cold, dark room.\n")
        print("In front of you, you can see a doorway. In the middle of the room, a staircase to the upper floor.\n")
        print("A clear, even voice echoes somewhere, not so distant, not so close.\n")
        print(f"'Hello {self.player.name}.'")
        print(
            "'Do not trouble yourself with questions of who you are, and why you are here. You are here, "
            "in this Tower, and there is no way out but through. Climb the tower. Reach the end. I will explain "
            "everything then.\n")
        input("Press enter to continue.")

    def proceed(self):
        os.system('printf "\033c"')
        self.map.display_map()
        print(self.map.access_current_room().description)
        self.move_player()


class Player:
    def __init__(self, name: str):
        self.name = name


class Challenge:
    def __init__(self):
        self.cleared = False

    def describe(self):
        if self.cleared is False:
            print("You must clear this challenge.")
        else:
            print("You have cleared this challenge.")


class Monster(Challenge):
    ranges = [(1, 5), (2, 5), (5, 9), (3, 10), (2, 4), (1, 2), (4, 9)]

    def __init__(self):
        super().__init__()
        self.health = random.choice([30, 40, 50, 60])
        self.damage = random.choice(self.ranges)
        print(self.damage)

    def fight(self, damage_range):
        if self.health <= 0:
            print("The monster is dead.")
        else:
            damage_dealt_to_monster = random.randint(*damage_range)
            damage_dealt_to_player = random.randint(*self.damage)
            self.health -= damage_dealt_to_monster
            print(f"Monster takes {damage_dealt_to_monster} dmg and deals {damage_dealt_to_player} dmg!")
            if self.health <= 0:
                print("Monster has died from its wounds.")
            else:
                print(f"Monster has {self.health} HP left.")


class Room:
    def __init__(self):
        self.description = random.choice(ROOM_DESCRIPTIONS)
        self.player_is_here = False
        self.end_room = False

    def show_on_map(self):
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

    def access_current_room(self):
        return self.layout[self.current_pos[0]][self.current_pos[1]]

    def move_player(self, proposed_position):
        try:
            if 0 > proposed_position[0] or proposed_position[0] >= self.height or 0 > proposed_position[1] or \
                    proposed_position[1] >= self.length:
                raise ValueError("Move out of bounds")

            self.layout[proposed_position[0]][proposed_position[1]].player_is_here = True
            self.layout[self.current_pos[0]][self.current_pos[1]].player_is_here = False
            self.current_pos = proposed_position
        except:
            input("Your move is invalid, please try again. Press enter to continue.")

    def create_map(self):
        for x in range(self.height):
            self.layout.append([Room() for y in range(self.length)])

    def display_map(self):
        for x in range(self.height):
            for y in range(self.length):
                print(self.layout[x][y].show_on_map(), end=" ")
            print("")


def main():
    # input_name = input("What is your name? Press Enter to select the default name.")
    # player_name = input_name if input_name is not "" else "Chadwick Feeserton"
    player_name = "Chadwick Feeserton"
    game = Game(player_name)
    game.begin()
    game.proceed()
    game.move_player()


main()
