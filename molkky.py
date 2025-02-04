"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Sara Nurminen
Student ID: 50224946
Email: sara.nurminen@tuni.fi

Mölkky-game
"""


# TODO:
# a) Implement the class Player here.
class Player:
    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__throws = []


    def add_points(self, round_points):

        self.__throws.append(round_points)

        if self.__points == 0:
            self.__points = round_points
        else:
            self.__points += round_points
        if self.__points > 39 and self.__points < 50:
            print(f"{self.__name} needs only {50 - self.__points} "
                  f"points. It's better to avoid knocking down the pins with higher points.")

    def get_name(self):

        return self.__name

    def get_points(self):

        return self.__points

    def has_won(self):
        if self.__points == 50:
            return True

        if self.__points > 50:
                self.__points = 25
                print(f"{self.__name} gets penalty points!")

    def mean(self):
        """

        :return:
        """

        if len(self.__throws) <= 1:
            return False

        mean = sum(self.__throws) / len(self.__throws)

        if mean < self.__throws[-1]:
            return True

        return False

    def pros(self):
        """

        :return:
        """
        if len(self.__throws) == 0:
            return 0.0

        return ((len(self.__throws) - self.__throws.count(0))
                / len(self.__throws)) * 100


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.

        if in_turn.mean():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.pros():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.pros():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
