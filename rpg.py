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
            self.proceed()

        self.map.move_player(proposed_position)
        self.proceed()

    def begin(self):
        os.system('printf "\033c"')
        print("You awake with no memory of who you are in a cold, dark room.\n")
        print("In front of you, you can see a doorway. In the middle of the room, a staircase to the upper floor.\n")
        print("A clear, even voice echoes somewhere, not so distant, not so close.\n")
        print(f"'Hello {self.player.name}.'")
        print(
            "'Do not worry about why you are here. Climb the tower and reach the end. Everything will be explained.'\n")
        input("Press enter to continue.")

    def proceed(self):
        os.system('printf "\033c"')
        current_room = self.map.access_current_room()
        print(current_room.description)
        if not current_room.challenge.cleared:
            self.map.display_map()
            print(current_room.challenge.description)
            current_room.challenge.engage(self.player.damage_range)
        self.map.display_map()
        self.move_player()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.damage_range = (5, 10)


class Challenge:
    def __init__(self):
        self.cleared = False

    def describe(self):
        if self.cleared is False:
            print("You must clear this challenge.")
        else:
            print("You have cleared this challenge.")


class EmptyChallenge(Challenge):
    def __init__(self):
        super().__init__()
        self.cleared = True
        self.description = "There is no challenge in this room."


class Monster(Challenge):
    ranges = [(1, 5), (2, 5), (5, 9), (3, 10), (2, 4), (1, 2), (4, 9)]

    def __init__(self):
        super().__init__()
        self.health = random.choice([30, 40, 50, 60])
        self.damage = random.choice(self.ranges)
        self.description = "A big monster is in front of you."

    def engage(self, damage_range):
        actions = {
            1: {
                "name": "Attack",
                "description": "You attack the monster."
            },
            2: {
                "name": "Defend",
                "description": "You guard against the monster's attack."
            }
        }

        while self.health > 0:
            damage_dealt_to_monster = random.randint(*damage_range)
            damage_dealt_to_player = random.randint(*self.damage)
            self.health -= damage_dealt_to_monster
            print(f"Monster takes {damage_dealt_to_monster} dmg and deals {damage_dealt_to_player} dmg!")
            print(f"Monster has {self.health} HP left.")
            if self.health <= 0:
                print("Monster has died from its wounds.")
                self.cleared = True
                continue
            for key in actions.keys():
                print(f"{key}) {actions[key]['name']}: {actions[key]['description']}")
            input(f"Type 1 of {list(actions.keys())} and press Enter to continue")
            if input in actions.keys():
                continue
        self.cleared = True
        print("The monster is dead.")


class Room:
    def __init__(self, challenge: Challenge):
        self.description = random.choice(ROOM_DESCRIPTIONS)
        self.player_is_here = False
        self.end_room = False
        self.challenge = challenge

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
            self.layout.append([Room(Monster()) for y in range(self.length)])
        self.layout[self.height - 1][0] = Room(EmptyChallenge())
        self.layout[0][self.length - 1].end_room = True

    def display_map(self):
        for x in range(self.height):
            for y in range(self.length):
                print(self.layout[x][y].show_on_map(), end=" ")
            print("")


def main():
    input_name = input("What is your name? Press Enter to select the default name.")
    player_name = input_name if input_name is not "" else "Chadwick Feeserton"
    game = Game(player_name)
    game.begin()
    game.proceed()


main()
