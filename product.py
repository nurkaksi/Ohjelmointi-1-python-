"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Sara Nurminen
Student ID: 50224946
Email: sara.nurminen@tuni.fi
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    def __init__(self, name, price, discount=0):
        self.__name = name
        self.__price = price
        self.__discount = discount

    def set_sale_percentage(self, discount):
        self.__discount = discount

    def printout(self):
        print(f"{self.__name}")
        print(f"  price: {self.__price}")
        print(f"  sale%: {self.__discount:.2f}")

    def get_price(self):
        if self.__discount > 0:
            current_price = self.__price * (1 - self.__discount/100)
        else:
            current_price = self.__price

        return current_price


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
