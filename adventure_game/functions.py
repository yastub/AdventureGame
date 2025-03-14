import time
import random
import sys
#Global constants for game state
TOTAL_SCORE = 0
LOST_TURNS = 0
DRAGON_HEALTH = 80
PLAYER_HEALTH = 100
FINAL_RESULT = 0
STORY_PROGRESS = 0
I = 0
REPLAY_ONE = 0

def check_game_status() -> tuple:
    #Checks the health of the player and the dragon.
    #Determines if the game should continue or if the player won or lost.
    #Returns:
    #tuple: (BM, REPLAY_ONE, I) where BM indicates game status,
    #REPLAY_ONE indicates replay choice, and I is a flag.
    global PLAYER_HEALTH, DRAGON_HEALTH, I, STORY_PROGRESS, REPLAY_ONE
    if PLAYER_HEALTH <= 0:
        print(" YOU DIED...")
        time.sleep(0.5)
        print(f"YOUR points : {TOTAL_SCORE}")
        time.sleep(0.5)
        print(f"DRAGONS HEALTH : {DRAGON_HEALTH}")
        time.sleep(0.5)
        print("Do you want to replay the game?")
        time.sleep(0.5)
        print("YES press 1")
        time.sleep(0.5)
        print("NO press 2")
        REPLAY_ONE = give_two_choice()
        BM = 1
        I = 1
    elif DRAGON_HEALTH <= 0:
        time.sleep(0.5)
        print("YOU WON! CONGRATULATIONS!")
        time.sleep(0.5)
        print(f"YOUR points : {TOTAL_SCORE}")
        time.sleep(0.5)
        print(f"YOUR HEALTH : {PLAYER_HEALTH}")
        time.sleep(0.5)
        print("Do you want to replay the game?")
        time.sleep(0.5)
        print("YES press 1")
        time.sleep(0.5)
        print("NO press 2")
        REPLAY_ONE = give_two_choice()
        STORY_PROGRESS += 1
        BM = 1
        I = 1
    else:
        BM = 0
    return BM, REPLAY_ONE, I
def deal_dragon_damage() -> int:
    #Simulates the dragon's attack on the player.
    #Returns:
    #int: Updated player health after taking damage.
    global PLAYER_HEALTH
    print("This dragon seems weak; it only damaged you 15 points")
    PLAYER_HEALTH -= 15
    return PLAYER_HEALTH
def dancing_edge() -> int:
    #Performs the "Dancing Edge" attack on the dragon,
    #with damage based on a random roll.
    #Returns:
    #int: Updated dragon health after taking damage.
    random_int = random.randint(1, 6)
    global TOTAL_SCORE, DRAGON_HEALTH
    damage_map = {
        1: 6,
        2: 12,
        3: 18,
        4: 24,
        5: 30,
        6: 36
    }
    if random_int >= 4:
        TOTAL_SCORE = add_total_score()
    print(f"YOU GET : {random_int}")
    if random_int == 6:
        print("you got super luck and dealt 36 damage")
        DRAGON_HEALTH -= 36
    elif random_int == 5:
        print("you got lucky and dealt 30 damage points")
        DRAGON_HEALTH -= 30
    elif random_int == 4:
        print("you got lucky and dealt 24 damage points")
        DRAGON_HEALTH -= 24
    elif random_int == 3:
        print("you got unlucky and dealt 18 damage points")
        DRAGON_HEALTH -= 18
    elif random_int == 2:
        print("you got unlucky and dealt 12 damage points")
        DRAGON_HEALTH -= 12
    elif random_int == 1:
        print("you got unlucky and dealt 6 damage points")
        DRAGON_HEALTH -= 6
    return DRAGON_HEALTH
def opening_thread() -> int:
    #Performs the "Opening Thread" attack,
    #determining damage based on a random roll.
    #Returns:
    #int: Updated dragon health after taking damage.
    random_int = random.randint(1, 6)
    global TOTAL_SCORE, DRAGON_HEALTH, PLAYER_HEALTH
    if random_int > 2:
        print(f"YOU GET : {random_int}")
        slow_type("You are lucky; you hit the dragon and dealt 15 damage.")
        print("And you didn't get damaged + 1 points.")
        TOTAL_SCORE = add_total_score()
        DRAGON_HEALTH -= 15
    else:
        print(f"YOU GET : {random_int}")
        slow_type("You got unlucky and some damage affected you.")
        print("But you dealt 15 damage.")
        DRAGON_HEALTH -= 15
        PLAYER_HEALTH -= 5
    return DRAGON_HEALTH
def slash_and_dash() -> int:
    #Performs the "Slash and Dash" attack,
    #determining damage based on a random roll.
    #Returns:
    #int: Updated dragon health after taking damage.
    random_int = random.randint(1, 6)
    global DRAGON_HEALTH, TOTAL_SCORE
    if random_int > 3:
        print(f"YOU GET : {random_int}")
        slow_type("You are lucky; you hit the dragon and")
        slow_type(" dealt 30 damage + 1 points.")
        TOTAL_SCORE = add_total_score()
        DRAGON_HEALTH -= 30
    else:
        print(f"YOU GET : {random_int}")
        slow_type("You got unlucky and you missed.")
        print("The hit - 1 points.")
        TOTAL_SCORE = sub_total_score()
    return DRAGON_HEALTH
def add_total_score() -> int:
    #Increases the player's total score by 1.
    #Returns:
    #int: Updated total score.
    global TOTAL_SCORE
    TOTAL_SCORE += 1
    return TOTAL_SCORE
def sub_total_score() -> int:
    #Decreases the player's total score by 1.
    #Returns:
    #int: Updated total score.
    global TOTAL_SCORE
    TOTAL_SCORE -= 1
    return TOTAL_SCORE
def give_one_choice() -> int:
    #Prompts the user for a single choice input.
    #Validates input to ensure it's an integer.
    #Returns:
    #int: Validated user choice.
    while True:
        choice = input("YOUR CHOICE: ")
        try:
            choice = int(choice)
            if choice == 1:
                time.sleep(1)
                print("Processing...")
                time.sleep(2)
                return choice
            elif choice > 1:
                time.sleep(1)
                print("Please enter an available choice.")
        except ValueError:
            time.sleep(1)
            print("Please enter an available number.")
def give_two_choice() -> int:
    #Prompts the user for a two-choice input.
    #Validates input to ensure it's an integer.
    #Returns:
    #int: Validated user choice.

    while True:
        choice = input("YOUR CHOICE: ")
        try:
            choice = int(choice)
            if choice in [1, 2]:
                time.sleep(1)
                print("Processing...")
                time.sleep(2)
                return choice
            elif choice > 2:
                time.sleep(1)
                print("Please enter an available choice.")
        except ValueError:
            time.sleep(1)
            print("Please enter an available number.")
def give_three_choice() -> int:
    #Prompts the user for a three-choice input.
    #Validates input to ensure it's an integer.
    #Returns:
    #int: Validated user choice.
    while True:
        choice = input("YOUR CHOICE: ")
        try:
            choice = int(choice)
            if choice in [1, 2, 3]:
                time.sleep(1)
                print("Processing...")
                time.sleep(2)
                return choice
            elif choice > 3:
                time.sleep(1)
                print("Please enter an available choice.")
        except ValueError:
            time.sleep(1)
            print("Please enter an available number.")
def give_four_choice() -> int:
    #Prompts the user for a four-choice input.
    #Validates input to ensure it's an integer.
    #Returns:
    #int: Validated user choice.
    while True:
        choice = input("YOUR CHOICE: ")
        try:
            choice = int(choice)
            if choice in [1, 2, 3, 4]:
                time.sleep(1)
                print("Processing...")
                time.sleep(2)
                return choice
            elif choice > 4:
                time.sleep(1)
                print("Please enter an available choice.")
        except ValueError:
            time.sleep(1)
            print("Please enter an available number.")
def main_menu() -> int:
    #Displays the main menu and prompts the user for a menu choice.
    #Returns:
    #int: The selected menu choice.
    time.sleep(1)
    print("  Welcome to ꜱʜᴀᴅᴏᴡꜱ ᴏꜰ ᴛʜᴇ ꜰᴏʀɢᴏᴛᴛᴇɴ....")
    time.sleep(2)
    print("STORY MODE press 1")
    time.sleep(0.5)
    print("TRAINING MODE press 2 (Not implemented yet)")
    time.sleep(0.5)
    print("MINIGAMES MODE press 3 (Not implemented yet)")
    time.sleep(0.5)
    print("SHOP press 4 (Not implemented yet)")
    time.sleep(0.5)
    print("EXIT press 5  *ɴᴏᴛ ʀᴇᴄᴏᴍᴍᴇɴᴅᴇᴅ*")
    time.sleep(0.5)
    while True:
        menu_choice = input("YOUR CHOICE: ")
        try:
            menu_choice = int(menu_choice)
            if menu_choice == 1:
                time.sleep(0.5)
                slow_type("Processing...")
                time.sleep(2)
                return menu_choice
            elif menu_choice == 5:
                time.sleep(1)
                print("Thank you for choosing our game.")
                return menu_choice
            elif menu_choice > 1:
                time.sleep(0.5)
                slow_type("Sorry, this option is not implemented yet.")
        except ValueError:
            time.sleep(1)
            slow_type("Please insert a number.")
def story_mode() -> int:
    #Displays the story mode menu and prompts the user for a chapter choice.
    #Returns:
    #int: The selected chapter choice.
    print(".")
    print("WELCOME TO THE STORY MODE...")
    time.sleep(0.5)
    print("CHAPTER 1 press 1")
    time.sleep(0.5)
    print("CHAPTER 2 press 2   *not implemented yet*")
    time.sleep(0.5)
    print("CHAPTER 3 press 3   *not implemented yet*")
    time.sleep(0.5)
    print("CHAPTER 4 press 4   *not implemented yet*")
    time.sleep(0.5)
    print("RETURN TO THE MAIN MENU press 5")
    time.sleep(0.5)
    while True:
        chapter_choice = input("YOUR CHOICE: ")
        try:
            chapter_choice = int(chapter_choice)
            if chapter_choice == 1:
                time.sleep(0.5)
                print("Processing...")
                time.sleep(2)
                return chapter_choice
            elif chapter_choice == 5:
                time.sleep(0.2)
                slow_type("Returning to the main menu...")
                time.sleep(2)
                return chapter_choice
            elif chapter_choice < 6:
                time.sleep(0.5)
                slow_type("This chapter is not implemented yet.")
            elif chapter_choice > 6:
                time.sleep(0.5)
                slow_type("Please, choose an available option.")
        except ValueError:
            time.sleep(0.5)
            print("Please, put a number.")
            time.sleep(1)
def slow_type(text: str) -> None:
    #Simulates typing effect for displaying text.
    #Args:
    #text (str): The string to display with typing effect.
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def chapter_one() -> int:
    #Handles the first chapter of the game,
    #including tutorial and initial encounters.
    #Returns:
    #int: The replay choice after completing the chapter.
    global PLAYER_HEALTH, DRAGON_HEALTH, TOTAL_SCORE, I, REPLAY_ONE
    time.sleep(0.4)
    print("FOR TUTORIAL press 1")
    print("FOR SKIPPING press 2")
    tut_choice = give_two_choice()
    if tut_choice == 1:
        print("           TUTORIAL...")
        time.sleep(0.5)
        slow_type("Quick tutorial: You will spawn with only a wooden sword, ")
        slow_type("a small shield. Through the game, you will find ")
        slow_type("weapons, armor, and even treasures, and you can fight ")
        slow_type("various types of enemies. When you are in a fight, it ")
        slow_type("will go by turn; each turn you will have to attack ")
        slow_type("or run, and with each attack, a dice will be rolled. ")
        slow_type("Depending on the number you got, it will give the ")
        slow_type("enemy damage. *Remember you have 100 health points... ")
        slow_type("1 is the worst and 6 is the best..")
        time.sleep(3)
    time.sleep(2)
    print("FOR STORY press 1")
    print("FOR SKIPPING press 2")
    sto_choice = give_two_choice()
    if sto_choice == 1:
        slow_type("You woke up in a boat and there were two people with ")
        slow_type("you, and you don't know them. One of them tries to wake ")
        slow_type("you up and calling you Rayligh... Rayligh and says ")
        slow_type("please wake up.. in an emotional tone. In the other ")
        slow_type("hand, the other person was looking through an old ")
        slow_type("scope to the horizon and saying .... hey hey, I found ")
        slow_type("an island. After you wake up, you don't remember ")
        slow_type("anything, and it seems like your memory is vanished. ")
        slow_type("But you asked them what happened and they told ")
        slow_type("you that they are on a mission to find a treasure ")
        slow_type("on the island they found before. Those people seem ")
        slow_type("like they are your friends. After some time, the ")
        slow_type("weather got worse and worse. But sadly the boat ")
        slow_type("sank, and you were able to swim to the island, but ")
        slow_type("your friends didn't make it:")
        time.sleep(4)
    print("Now only you and the shipwrecks that had a wooden sword, ")
    slow_type("armor, and some food.")
    time.sleep(1)
    slow_type("Now you find yourself in front of a cave.")
    print(".")
    time.sleep(1)
    print("ENTER THE CAVE press 1 *only choice*")
    choice = give_one_choice()
    slow_type("You can't see anything except a faint sparkly white ")
    slow_type("far from you; you go and check what's this. You found ")
    slow_type("a strange looking sword, and it's made of stone. ")
    print(".")
    slow_type("Do you want to equip it?")
    print(".")
    time.sleep(1)
    print("YES press 1")
    time.sleep(0.3)
    print("NO press 2")
    time.sleep(1)
    choice = give_two_choice()
    if choice == 1:
        TOTAL_SCORE = add_total_score()
        slow_type("YOU BECAME STRONGER and now your ")
        slow_type("base damage = 15, + 1 point")
        print(".")
        print(f" YOUR points: {TOTAL_SCORE}")
        time.sleep(1)
    elif choice == 2:
        TOTAL_SCORE = sub_total_score()
        print("You missed the opportunity, - 1 point")
        print(f" YOUR points: {TOTAL_SCORE}")
        time.sleep(1)
    slow_type("After that you go deeper into the cave, but no luck. After ")
    slow_type("some time, you hear a strange voice, but you went to check ")
    slow_type("it and you found a strange small dragon, but sadly ")
    slow_type("this dragon wants to fight.")
    print(".")
    time.sleep(1)
    print("FIGHT press 1")
    time.sleep(0.5)
    print("RUN AND RETREAT press 2")
    while I == 0:
        choice3 = give_two_choice()
        if choice3 == 1:
            BM = 0
            while BM == 0:
                time.sleep(1)
                slow_type("NOW it's your turn. You can only do ")
                slow_type("three moves with your sword.")
                print(".")
                slow_type("SLASH AND DASH press 1  *double damage but ")
                slow_type("if you get lower than 3 you will miss the hit*")
                print(".")
                slow_type("OPENING THREAD press 2 *decent damage but ")
                slow_type("if you get lower than or 2 some damage will ")
                slow_type("be reflected to you*")
                print(".")
                slow_type("DANCING EDGE press 3 *low damage but ")
                slow_type("gives strikes as the same amount of ")
                slow_type("what you get on the dice*")
                print(".")
                print("SHOW PLAYER'S INFO press 4")
                choice4 = give_four_choice()
                if choice4 == 1:
                    DRAGON_HEALTH = slash_and_dash()
                    print(f" DRAGONS HEALTH: {DRAGON_HEALTH}")
                    print(f" YOUR points: {TOTAL_SCORE}")
                    time.sleep(1)
                    I, REPLAY_ONE, BM = check_game_status()
                    if I == 1:
                        continue
                    PLAYER_HEALTH = deal_dragon_damage()
                    print(f" YOUR HEALTH: {PLAYER_HEALTH}")
                elif choice4 == 2:
                    DRAGON_HEALTH = opening_thread()
                    print(f" DRAGONS HEALTH: {DRAGON_HEALTH}")
                    print(f" YOUR points: {TOTAL_SCORE}")
                    print(f" YOUR HEALTH: {PLAYER_HEALTH}")
                    time.sleep(1)
                    I, REPLAY_ONE, BM = check_game_status()
                    if I == 1:
                        continue
                    PLAYER_HEALTH = deal_dragon_damage()
                    print(f" YOUR HEALTH: {PLAYER_HEALTH}")
                elif choice4 == 3:
                    DRAGON_HEALTH = dancing_edge()
                    print(f" DRAGONS HEALTH: {DRAGON_HEALTH}")
                    print(f" YOUR HEALTH: {PLAYER_HEALTH}")
                    print(f" YOUR points: {TOTAL_SCORE}")
                    time.sleep(1)
                    I, REPLAY_ONE, BM = check_game_status()
                    if I == 1:
                        continue
                    PLAYER_HEALTH = deal_dragon_damage()
                    print(f" YOUR HEALTH: {PLAYER_HEALTH}")
                elif choice4 == 4:
                    print(f" YOUR HEALTH: {PLAYER_HEALTH}")
                    time.sleep(1)
                    print(f" DRAGONS HEALTH: {DRAGON_HEALTH}")
                    time.sleep(1)
                    print(f" YOUR points: {TOTAL_SCORE}")
        elif choice3 == 2:
            slow_type("You tried to run out of the cave, but ")
            slow_type("the dragon followed you, and he is faster.")
            slow_type(" You must fight.  * - 1 point ")
            TOTAL_SCORE = sub_total_score()
            print("FIGHT press 1")
            time.sleep(0.5)
            print("RUN AND RETREAT press 2")
            continue
    return REPLAY_ONE