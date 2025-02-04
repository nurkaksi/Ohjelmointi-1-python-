"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Sara Nurminen
sara.nurminen@tuni.fi
050224946
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

        self.__numerator = numerator
        self.__denominator = denominator

    def get_numerator(self):
        return int(self.__numerator)

    def get_denominator(self):
        return int(self.__denominator)

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


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


    def simplify(self):

        a = greatest_common_divisor(self.__numerator, self.__denominator)
        numerator = self.__numerator // a
        denominator = self.__denominator // a
        return Fraction(numerator, denominator)

    def complement(self):
            complement_numerator = int(- self.get_numerator())
            complement_fraction = Fraction(complement_numerator, self.get_denominator())
            return complement_fraction

    def reciprocal(self):
        return Fraction(self.get_denominator(), self.get_numerator())

    def multiply(self, kohde):
        numerator = self.__numerator * kohde.__numerator
        denominator = self.__denominator * kohde.__denominator
        return Fraction(numerator, denominator)

    def divide(self, kohde):
        kohde1 = kohde.reciprocal()
        vastaus = self.multiply(kohde1)
        return vastaus

    def add(self, kohde):

        numerator = (self.__numerator * kohde.__denominator +
                     kohde.__numerator * self.__denominator)

        denominator = (self.__denominator * kohde.__denominator)

        return Fraction(numerator, denominator)



    def deduct(self, kohde):
        numerator = (self.__numerator * kohde.__denominator -
                     kohde.__numerator * self.__denominator)

        denominator = (self.__denominator * kohde.__denominator)

        return Fraction(numerator, denominator)

    def __lt__(self, other):
        # check if self is less than other
        return (self.get_numerator() * other.get_denominator() <
                other.get_numerator() * self.get_denominator())

    def __gt__(self, other):
        # check if self is greater than other
        return (self.get_numerator() * other.get_denominator() >
                other.get_numerator() * self.get_denominator())



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

def ask_fractions():
    """
    function asks user to input fractions and simplifies them
    """
    fractions = []  # lista murtolukuolioille

    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")

    while True:
        input_str = input()
        if not input_str:  # lopetetaan tyhjällä syötteellä
            break

        try:
            # Jäsennellään osoittaja ja nimittäjä käyttäen split-metodia
            numerator_str, denominator_str = input_str.split('/')
            numerator = int(numerator_str)
            denominator = int(denominator_str)

            # Muodostetaan uusi murtolukuolio ja lisätään se listaan
            fraction = Fraction(numerator, denominator)
            fractions.append(fraction)
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter fractions in the format integer/integer.")

    print("The given fractions in their simplified form:")
    for fraction in fractions:
        simplified = fraction.simplify()
        print(f"{fraction.return_string()} = {simplified.return_string()}")
def main():
    pass

if __name__ == "__main__":
        main()
