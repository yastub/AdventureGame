from functions import *
x = 0
while x ==0:
    menu_choice = main_menu()
    z = 0
    w = 0
    if menu_choice == 1:
        while z == 0:
            story_choice = story_mode()
            if story_choice == 1:
                while w == 0:
                    replay_choice = chapter_one()
                    if replay_choice == 1:
                        continue
                    else :
                        print("redirecting to the main menu")
                        w = 1
                        z = 1
                        continue
            else:
                z = 1
                continue
    else:
        x = 1