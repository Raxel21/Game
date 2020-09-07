from os import system, name

# Check the system, to use the correct
# command that cleans the console
def clear():
    if name == "nt":
        s = system("cls")
    else:
        s = system("clear")
