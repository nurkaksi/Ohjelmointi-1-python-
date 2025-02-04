"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Sara Nurminen
Student ID: 50224946
Email: sara.nurminen@tuni.fi
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        if denominator < 0 and numerator > 0:
            self.__numerator = numerator * -1
            self.__denominator = denominator * -1
        elif denominator < 0 and numerator < 0:
            self.__numerator = abs(numerator)
            self.__denominator = abs(denominator)
        else:
            self.__numerator = numerator
            self.__denominator = denominator



    def __str__(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


    def multiply(self, frac2):
        """

        :return:
        """
        return Fraction(self.__numerator * frac2.get_numerator(),
                        self.__denominator * frac2.get_denominator())


    def simplify(self):
        """
        :return:
        """
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)

        self.__numerator = self.__numerator // divisor
        self.__denominator = self.__denominator // divisor


    def get_numerator(self):
        """

        :return:
        """
        return self.__numerator

    def get_denominator(self):
        """

        :return:
        """
        return self.__denominator



def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    all_answers = {}

    while True:
        answer = input("> ")
        if answer == "quit":
            print("Bye bye!")
            break

        elif answer == "add":
            fraction_answer = input("Enter a fraction in the form integer/integer: ")
            fraction_name = input("Enter a name: ")
            all_answers[fraction_name] = fraction_answer

        elif answer == "print":
            print_name = input("Enter a name: ")
            if print_name not in all_answers:
                print(f"Name {print_name} was not found")
            else:
                print(f"{print_name} = {all_answers[print_name]}")

        elif answer == "list":
            if len(all_answers) == 0:
                continue
            else:
                for i in sorted(all_answers):
                    print(f"{i} = {all_answers[i]}")

        elif answer == "*":
            first = input("1st operand: ")
            if first not in all_answers:
                print(f"Name {first} was not found")
                continue
            second = input("2nd operand: ")
            if second not in all_answers:
                print(f"Name {second} was not found")
                continue

            frac1 = Fraction(int(all_answers[first].split("/")[0]),
                             int(all_answers[first].split("/")[1]))
            frac2 = Fraction(int(all_answers[second].split("/")[0]),
                             int(all_answers[second].split("/")[1]))
            multiplied = frac1.multiply(frac2)


            print(f"{all_answers[first]} * {all_answers[second]} = "
                  f"{multiplied}")
            multiplied.simplify()
            print(f"simplified {multiplied}")

        elif answer == "file":
            file = input("Enter the name of the file: ")
            try:
                open_file = open(file, mode="r")

                for line in open_file:
                    line = line.rstrip()
                    if "=" not in line or "/" not in line:
                        print("Error: the file cannot be read.")
                        continue
                    name, score = line.split("=")
                    all_answers[name] = score


            except FileNotFoundError:
                print("Error: the file cannot be read.")
                continue

            open_file.close()

        else:
            print("Unknown command!")



if __name__ == "__main__":
    main()
