from util import clear

# Checks that the user's response is an integer
# Return an integer


def int_input(message, clean=False):
    while True:
        try:
            m = int(input(message))
            return m
        except ValueError:
            if clean:
                clear()
            print("Only integers are accepted")