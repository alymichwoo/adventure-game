import time
import random


enemy_list = ["vampire", "troll", "pirate", "gorgon", "dragon"]
enemy = random.choice(enemy_list)


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(weapon):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")
    print_pause("")
    house_or_cave(weapon)


def house_or_cave(weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    player_choice(weapon)


def player_choice(weapon):
    choice = input("(Please enter 1 or 2.)")
    if choice == "1":
        house(weapon)
    elif choice == "2":
        cave(weapon)
    else:
        player_choice(weapon)


def house(weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " +
                enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    print_pause("You feel a bit under prepared for this, what with only having"
                " a tiny dagger.")
    fight_or_field(weapon)


def cave(weapon):
    print_pause("You peer cautiously into the cave.")
    if "sword" in weapon:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with"
                    " you.")
        weapon.append("sword")
    print_pause("You walk back out to the field.")
    print_pause("")
    house_or_cave(weapon)


def fight_or_field(weapon):
    fight_or_field = input("Would you like to (1) fight or (2) run away?")
    if fight_or_field == "1":
        fight(weapon)
    elif fight_or_field == "2":
        field(weapon)
    else:
        fight_or_field(weapon)


def fight(weapon):
    if "sword" in weapon:
        print_pause("As the " + enemy + " moves to attack, you unsheath your "
                    "new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause("But the " + enemy + " takes one look at your shiny new "
                    "toy and runs away!")
        print_pause("You have rid the town of the " + enemy + ". You are "
                    "victorious!")
        play_again(weapon)
    else:
        print_pause("You do your best...")
        print_pause("But your dagger is no match for the " + enemy + ".")
        print_pause("You have been defeated!")
        play_again(weapon)


def field(weapon):
    print_pause("You run back into the field. Luckily, you don't seem to have "
                "been followed.")
    print_pause("")
    house_or_cave(weapon)


def play_again(weapon):
    play_again = input("Would you like to play again? (y/n)")
    if play_again == "y":
        print_pause("Excellent! Restarting the game...")
        play_game()
    elif play_again == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again(weapon)


def play_game():
    weapon = []
    intro(weapon)


play_game()
