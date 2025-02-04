"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Sara Nurminen
Student ID: 50224946
Email: sara.nurminen@tuni.fi
"""

class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0
        self.__odometer = 0



    # TODO:
    # Add the definitions of all methods of this class here.
    # The methods are a part of the class. Therefore, they are intended on
    # this level (i.e. inside the class definition).

    # When printing the car status, use the following f-string to make
    # sure the printout is in the correct format to pass the automated tests:
    #
    #    f"The tank contains {:.1f} liters of gas and the odometer shows {:.1f} kilometers."
    #                         ^                                           ^
    #
    # You need to add the correct attributes to points marked with carets "^".

    def print_information(self):
        """
        Prints the amount af gas in tank and driven kilometers
        """
        print(f"The tank contains {self.__gas:.1f} liters of gas "
              f"and the odometer shows {self.__odometer:.1f} kilometers.")

    def fill(self, fuel_up):
        """
        Adds fuel to cars tank
        :param fuel_up: float, the amount of gas to be fueled
        """
        if fuel_up < 0:
            print("You cannot remove gas from the tank")
        elif self.__gas + fuel_up > self.__tank_volume:
            self.__gas = self.__tank_volume
        else:
            self.__gas += fuel_up

    def drive(self, distance):
        """
        Adds kilometers to odometer and reduces used gas from tank
        :param distance:
        """
        gas_used = (distance / 100) * self.__consumption
        if distance < 0:
            print("You cannot travel a negative distance")
        elif gas_used > self.__gas:
            real_distance = (self.__gas / self.__consumption) * 100
            self.__gas = 0
            self.__odometer += real_distance
        else:
            self.__gas -= gas_used
            self.__odometer += distance


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    # Here we define the variable car which is an object initiated
    # from the class Car (its type is Car). This is the point where the
    # constructor of the class Car (i.e. the method that is named __init__)
    # is called automatically behind the scenes to give an initial
    # value for the Car object we are creating!

    car = Car(tank_size, gas_consumption)

    # In this program we only need one car object but it is possible
    # to create multiple objects from one class. For example we could
    # create more objects if we needed them:
    #
    #     lightning_mcqueen = Car(20, 30)
    #     canyonero = Car(200, 400)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")

            # TODO:
            # call the fill-method for the car-object here (task b)
            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")

            # TODO:
            # call the drive-method for the car-object here (task c)
            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
