"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Sara Nurminen
Student ID: 50224946
Email: sara.nurminen@tuni.fi
"""


def main():

    filename = input("Enter the name of the score file: ")
    try:
        points_file = open(filename, mode="r")
    except FileNotFoundError:
        print("There was an error in reading the file.")
        return
    points_dict = {}
    for line in points_file:
        line = line.strip()
        try:
            name, points = line.split(" ")
        except ValueError:
            print("There was an erroneous line in the file:")
            print(line)
            return
        try:
            points = int(points)
        except ValueError:
            print("There was an erroneous score in the file:")
            print(points)
            return
        if name not in points_dict:
            points_dict[name] = points
        else:
            points_dict[name] += points


    print("Contestant score:")

    def payload(key):
        return points_dict[key]

    for name in sorted(points_dict):
        print(f"{name} {points_dict[name]}")




if __name__ == "__main__":
    main()
