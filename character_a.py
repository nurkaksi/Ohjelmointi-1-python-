"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Sara Nurminen
50224946
sara.nurminen@tuni.fi

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""


class Character:

    def __init__(self, name):
        self.__name = name
        self.__inventory = {}


    def give_item(self, item):
        if item not in self.__inventory:
            self.__inventory[item] = 1
        else:
            self.__inventory[item] += 1


    def remove_item(self, item):
        if item in self.__inventory:
            if self.__inventory[item] == 1:
                del self.__inventory[item]
            else:
                self.__inventory[item] -= 1


    def has_item(self, item):
        if item in self.__inventory:
            return True
        else:
            return False

    def printout(self):
        print(f"Name: {self.__name}")
        if self.__inventory == {}:
            print(f"  --nothing--")
        for item in sorted(self.__inventory):
            print(f"  {self.__inventory[item]} {item}")

    def how_many(self, item):
        if item in self.__inventory:
            return self.__inventory[item]
        else:
            return 0

    def get_name(self):
        return self.__name


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
