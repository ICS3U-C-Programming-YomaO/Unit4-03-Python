#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program asks the squares the user input


def main():

    # get user input
    user_num = input("Please enter a positive integer: ")

    try:
        # cast user num as int
        user_num = int(user_num)
        if user_num < 0:
            print("Please enter a positive integer.")

        else:

            # loop to square user input
            for counter in range(0, user_num + 1):
                square_value = counter**2

                # show the counter and square value
                print(f"{counter}² is {square_value}")

    # exception handling
    except ValueError:
        print(user_num, "is not an integer. Please enter a valid integer")

    # display ending message
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":

    main()
