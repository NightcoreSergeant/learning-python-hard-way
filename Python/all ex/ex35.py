from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number!")

    if how_much < 50:
        print("Nice you're not greedy, you win")
        exit(0)

    else:
        dead("You greedy bastard")


def bear_room():
    print("""
    There is a bear here
    The bear has bunch of honey
    The fat bear is at another door
    How are you going to move bear?
    """)
    bear_moved = False

    while True:
        next = input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has been moved")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means.")
        
def cthulhu_room():
    print("""
    Here you see the great evil cthulhu.
    do you flee for your life or eat your head?
    """)

    next = input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job")
    exit(0)

def start():
    print("""
    you are in dark room
    there is a door to your rigt and left
    which one do you take?
    """)

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()